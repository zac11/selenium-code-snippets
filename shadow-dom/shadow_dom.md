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
![Image](/Users/zac/Downloads/dom.png)

Image and HTML code credits - [Link](https://cosmocode.io/how-to-interact-with-shadow-dom-in-selenium/)


# SHADOW DOM

Shadow DOM is one of the implementations of the OOPS principle of Encapsulation in an HTML document or DOM if you will.
By using the concept of Shadow DOM, the style, behavior and actions on one part of the page can be completely hidden
or kept separate from other part of the DOM.

Shadow DOM allows hidden DOM trees to be attached to elements in the regular DOM tree — this shadow DOM tree starts 
with a shadow root, underneath which can be attached to any elements you want, in the same way as the normal DOM.

![DOM](/Users/zac/Downloads/shadow-dom.png)

There are some bits of shadow DOM terminology to be aware of:

- Shadow host: The regular DOM node that the shadow DOM is attached to.
- Shadow tree: The DOM tree inside the shadow DOM.
- Shadow boundary: the place where the shadow DOM ends, and the regular DOM begins.
- Shadow root: The root node of the shadow tree.
