# SHADOW DOM
For reference - https://stackoverflow.com/questions/37384458/how-to-handle-elements-inside-shadow-dom-from-selenium

# DOM
Before understanding the concept of Shadow DOM, let us take a quick look at what DOM means. DOM is an abbreviation
of Document Object Model

As per the Mozilla Developer Network this is what is a DOM is

```The Document Object Model (DOM) connects web pages to scripts or programming languages by representing the structure of a document—such as the HTML representing a web page—in memory. Usually it refers to JavaScript, even though modeling HTML, SVG, or XML documents as objects are not part of the core JavaScript language.

The DOM represents a document with a logical tree. Each branch of the tree ends in a node, and each node contains objects. DOM methods allow programmatic access to the tree. With them, you can change the document's structure, style, or content.

Nodes can also have event handlers attached to them. Once an event is triggered, the event handlers get executed.
```


Let us consider a very simple example of an HTML page

```<html lang="en">
 <head>
   <title>A simple web page</title>
  </head>
 <body>
    <h1>Hello world</h1>
    <p>I am rendered!</p>
  </body>
 </html>
```

As mentioned in the above mentioned definition, a logical tree of the this HTML structure would look this this

![DOM](https://i0.wp.com/cosmocode.io/wp-content/uploads/2020/05/dom.png?resize=768%2C697&ssl=1)


Image and HTML code credits - [Link](https://cosmocode.io/how-to-interact-with-shadow-dom-in-selenium/)


# SHADOW DOM

Shadow DOM is one of the implementations of the OOPS principle of Encapsulation in an HTML document or DOM if you will.
By using the concept of Shadow DOM, the style, behavior and actions on one part of the page can be completely hidden
or kept separate from other part of the DOM.

Shadow DOM allows hidden DOM trees to be attached to elements in the regular DOM tree — this shadow DOM tree starts 
with a shadow root, underneath which can be attached to any elements you want, in the same way as the normal DOM.

![DOM](https://i2.wp.com/mdn.mozillademos.org/files/15788/shadow-dom.png)

There are some bits of shadow DOM terminology to be aware of:

- Shadow host: The regular DOM node that the shadow DOM is attached to.
- Shadow tree: The DOM tree inside the shadow DOM.
- Shadow boundary: the place where the shadow DOM ends, and the regular DOM begins.
- Shadow root: The root node of the shadow tree.


# HOW IS SHADOW DOM ACCESSIBLE BY SELENIUM

Consider this piece of code, which contains a `shadow-dom`

```buildoutcfg
<div>
  <div id="shell">
  <div id="role-id"></div>
    #shadow-root (open)
      <div id="avatar"></div>
  </div>
  <a href="./logout.html">Logout</a>
</div>
```
In this HTML snippet, if we access the element with `id` as `role-id`, then we can do this via Selenium as
`driver.find_element(By.ID,'role-id')` or like this `driver.find_elment(By.CSS_SELECTOR,'#role-id')`
both of which are valid Selenium statements to get this WebElement.

However, doing this for the `shadow-dom` element
`driver.find_element(By.ID,'avatar')` or like this `driver.find_elment(By.CSS_SELECTOR,'#avatar')`
will result in a `NoSuchElementException` in Selenium.

To access the `shadow-dom` through Selenium, we'll have to fire plain JS statements using the 
`driver.execute_script()` method.

## SINGLE SHADOW DOM

We inject a piece of JavaScript into the browser to get the target element inside the shadow DOM. 
Once we have the target element we can parse it into a WebElement and can perform any valid operation on that element.

```buildoutcfg
host = driver.find_element_by_id("shell"))
shadowRoot = driver.execute_script("return arguments[0].shadowRoot", host)
shadowRoot.find_elemen_by.id("avatar")).click()
```

Now this will click on the element inside the `shadow-dom`. However it is not neccessary to have a single `shadow-dom`
in the parent DOM. There might be multiple `shadow-dom` inside the parent DOM and also nested `shadow-dom` (`shadow-dom` withon
 a `shadow-dom`)


## MULTIPLE or NESTED SHADOW DOM

Now consider this screenshot given below -

![Image](/Users/zac/Desktop/Screenshot 2021-08-26 at 8.40.03 PM.png)

As you can see there are multiple `shadow-dom` elements in this piece of code - where  in there are nested layers
of `shadow-dom`. Now the problem with first approach discussed here is there it if we try to access the contents of the 
nested `shadow-dom`, we cannot do that unless we expand the parent level `shadow-dom`. 

So in order to solve this issue, we need to expand multiple levels of `shadow-dom` trees to get to the desired element.

Now we can approach this in two ways -

- APPROACH 1

What we can do it combine a sequence of statements , which uses the hard-code way of appending the `shadow-dom` JS query
For eg - let's say we want to click on the Detection tab on this given [URL](https://www.virustotal.com/gui/file/03d1316407796b32c03f17f819cca5bede2b0504ecdb7ba3b845c1ed618ae934/details)

If we see the dom structure, we can use this query

```buildoutcfg
search_button = driver.execute_script('return document.querySelector("file-view").shadowRoot.querySelector("report").shadowRoot.querySelector("vt-ui-button[data-route="detection"]")
search_button.click()

```

However, this is very generic and has a lot of hard-coded elements, which makes this selector very brittle. However 
this is not incorrect, just not an optimised way of solving this issue.

- APPROACH 2

We'll create one function - that will expand the parent `shadow-dom` tree 

```buildoutcfg
def expand_shadow_root(element):
    shadow_root = driver.execute_script('return arguments[0].shadowRoot', element)
    return shadow_root

```
Upon calling on multiple iterations on the nested `shadow-dom` elements, this will expand the parent `shadow-dom`,
and then try to find any element if we want inside it and then perform any action on that element.

For the `Detection` tab click, 
- First we expand the `shadow-root` below the element with id `file-view`

```buildoutcfg
root2 = driver.find_element(By.ID,'file-view')
shadow_root_2 = expand_shadow_root(root2)
``` 
- Next, we expand the `shadow-dom` below the element with id `report`

```buildoutcfg
root3 = shadow_root_2.find_element(By.ID,'report')
shadow_root_3 = expand_shadow_root(root3)
```

Now the element that we want to click is inside the `shadow-dom`,so we'll use the following locator to find the
element and then click on it

```buildoutcfg
root4 = shadow_root_3.find_element(By.CSS_SELECTOR,'vt-ui-button[data-route="detection"]')
root4.click()
```

Try running this script on the system and it will click on the `Detection` tab successfully.

Note - The code is written as per the changes for Selenium 4 (which is in final beta now), and that is why there may be
some subtle changes in how Chromedriver is initialised.