# CSS
### CSS Cheat Sheet
[Learn CSS_ Syntax and Selectors Cheatsheet _ Codecademy.pdf](https://github.com/gustavoalito/BeCode/blob/main/Phishing/2.making_phishing/Learn%20CSS_%20Syntax%20and%20Selectors%20Cheatsheet%20_%20Codecademy.pdf)

---

## Internal stylesheet (nested within the "head" tag)

An internal stylesheet has certain benefits and use cases over inlines styles, but once again, it’s not best practice (we’ll get there, we promise). Understanding how to use internal stylesheets is nonetheless helpful knowledge to have.

To create an internal stylesheet, a "style" element must be placed inside of the "head" element.

![image](https://github.com/gustavoalito/BeCode/assets/133368766/289017d4-dfb4-43e0-b4fb-63da6d741c95)


The CSS code in the example above changes the color of all paragraph text to red and also changes the size of the text to 20 pixels. Note how the syntax of the CSS code matches (for the most part) the syntax you used for inline styling. The main difference is that you can specify which elements to apply the styling.


When HTML and CSS codes are in separate files, the files must be linked. Otherwise, the HTML file won’t be able to locate the CSS code, and the styling will not be applied.

You can use the [`<link>`](https://www.codecademy.com/resources/docs/html/elements/link?page_req=catalog) element to link HTML and CSS files together. The `<link>` element must be placed within the head of the HTML file. It is a self-closing tag and requires the following attributes:

1. `href` — like the anchor element, the value of this attribute must be the address, or path, to the CSS file.
2. `rel` — this attribute describes the relationship between the HTML file and the CSS file. Because you are linking to a stylesheet, the value should be set to `stylesheet`.

When linking an HTML file and a CSS file together, the `<link>` element will look like the following:
![image](https://github.com/gustavoalito/BeCode/assets/133368766/513b8907-eb15-40be-9c77-aff80ba79c7c)


Note that the the path to the stylesheet is a URL.

Specifying the path to the stylesheet using a URL is one way of linking a stylesheet.

If the CSS file is stored in the same directory as your HTML file, then you can specify a relative path instead of a URL, like so:

![image](https://github.com/gustavoalito/BeCode/assets/133368766/665a571d-19a1-4e69-8a5c-05785e61172b)


Using a relative path is very common way of linking a stylesheet.

## Universal

The _universal selector_ selects all elements of _any_ type. The universal selector uses the `*` character in the same place where you specified the type selector in a ruleset, like so:
![image](https://github.com/gustavoalito/BeCode/assets/133368766/4e394582-9e28-461b-9579-d0abe48633a2)

In the code above, every text element on the page will have its **font** changed to `Verdana`.


## Class

CSS is not limited to selecting elements by their type. As you know, HTML elements can also have [attributes](https://www.codecademy.com/courses/learn-html/lessons/intro-to-html/exercises/attr-html). When working with HTML and CSS a [_class_](https://www.codecademy.com/resources/docs/html/classes?page_req=catalog) attribute is one of the most common ways to select an element.

For example, consider the following HTML:
![image](https://github.com/gustavoalito/BeCode/assets/133368766/5f3d23d8-cb1b-4a72-96ad-9875fe1ced3b)


The paragraph element in the example above has a `class` attribute within the opening tag of the`<p>` element. The `class` attribute is set to `'brand'`. To select this element using CSS, we can create a ruleset with a class selector of `.brand`.

![image](https://github.com/gustavoalito/BeCode/assets/133368766/0d025795-dc76-492f-8d70-30d74c18f9e7)

To select an HTML element by its class using CSS, a period (`.`) must be prepended to the class’s name. In the example above, the class is `brand`, so the CSS selector for it is `.brand`.

## Multiple Classes

It’s possible to add more than one class name to an HTML element’s `class` attribute.

For instance, perhaps there’s a heading element that needs to be green and bold. You could write two CSS rulesets like so:
![image](https://github.com/gustavoalito/BeCode/assets/133368766/85b671d7-21e9-4517-b770-0724c2ed01d9)


Then, you could include both of these classes on one HTML element like this:

![image](https://github.com/gustavoalito/BeCode/assets/133368766/a5986d87-9541-49d9-b348-01d407d65083)


We can add multiple classes to an HTML element’s `class` attribute by separating them with a space. This enables us to mix and match CSS classes to create many unique styles without writing a custom class for every style combination needed.

## ID

Oftentimes it’s important to select a single element with CSS to give it its own unique style. If an HTML element needs to be styled uniquely, we can give it an ID using the `id` attribute.

![image](https://github.com/gustavoalito/BeCode/assets/133368766/701b272a-cf23-4332-958b-c6ccbf899aca)


n contrast to `class` which accepts multiple values, and can be used broadly throughout an HTML document, an element’s `id` can only have a single value, and only be used once per page.

To select an element’s ID with CSS, we prepend the `id` name with a number sign (`#`). For instance, if we wanted to select the HTML element in the example above, it would look like this:

![image](https://github.com/gustavoalito/BeCode/assets/133368766/158dfc70-e4d1-4ab8-b5fd-656c526e1da4)


The `id` name is `large-title`, therefore the CSS selector for it is `#large-title`.

## Attribute

You may remember that some HTML elements use attributes to add extra detail or functionality to the element. Some familiar attributes may be `href` and `src`, but there are [many more](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes)—including `class` and `id`!

The _attribute selector_ can be used to target HTML elements that already contain attributes. Elements of the same type can be targeted differently by their attribute or attribute value. This alleviates the need to add new code, like the `class` or `id` attributes.

Attributes can be selected similarly to types, classes, and IDs.

## Attribute

You may remember that some HTML elements use attributes to add extra detail or functionality to the element. Some familiar attributes may be `href` and `src`, but there are [many more](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes)—including `class` and `id`!

The _attribute selector_ can be used to target HTML elements that already contain attributes. Elements of the same type can be targeted differently by their attribute or attribute value. This alleviates the need to add new code, like the `class` or `id` attributes.

Attributes can be selected similarly to types, classes, and IDs.

![image](https://github.com/gustavoalito/BeCode/assets/133368766/1424789c-4a70-470a-9645-df96a31d5318)


The most basic syntax is an attribute surrounded by square brackets. In the above example: `[href]` would target all elements with an `href` attribute and set the [`color`](https://www.codecademy.com/resources/docs/css/colors/color) to `magenta`.

And it can get [more granular](https://developer.mozilla.org/en-US/docs/Web/CSS/Attribute_selectors#syntax) from there by adding type and/or attribute values. One way is by using `type[attribute*=value]`. In short, this code selects an element where the attribute contains any instance of the specified value. Let’s take a look at an example.
![image](https://github.com/gustavoalito/BeCode/assets/133368766/92789f55-f884-46be-b2a7-ee3ab4a07099)


The HTML code above renders two [`<img>`](https://www.codecademy.com/resources/docs/html/elements/img?page_req=catalog) elements, each containing a `src` attribute with a value equaling a link to an image file.

![image](https://github.com/gustavoalito/BeCode/assets/133368766/98851953-a30c-4dbc-b20b-e106e877c709)


Now take a look at the above CSS code. The _attribute selector_ is used to target each image individually.

- The first ruleset looks for an `img` element with an attribute of `src` that contains the string `'winter'`, and sets the [`height`](https://www.codecademy.com/resources/docs/css/sizing/height) to `50px`.
- The second ruleset looks for an `img` element with an attribute of `src` that contains the string `'summer'`, and sets the `height` to `100px`.

Notice how no new HTML markup (like a class or id) needed to be added, and we were still able to modify the styles of each image independently. This is one advantage to using the attribute selector!

## Pseudo-class

You may have observed how the appearance of certain elements can change, or be in a different state, after certain user interactions. For instance:

- When you click on an `<input>` element, and a blue [border](https://www.codecademy.com/resources/docs/css/borders/border) is added showing that it is in _focus_.
- When you click on a blue `<a>` link to _visit_ to another page, but when you return the link’s text is purple.
- When you’re filling out a form and the submit button is grayed out and _disabled_. But when all of the fields have been filled out, the button has color showing that it’s _active_.

These are all examples of pseudo-class [selectors](https://www.codecademy.com/resources/docs/css/selectors) in action! In fact, `:focus`, `:visited`, `:disabled`, and `:active` are all [pseudo-classes](https://www.codecademy.com/resources/docs/css/pseudo-classes). Factors such as user interaction, site navigation, and position in the document tree can all give elements a different state with pseudo-class.

A pseudo-class can be attached to any selector. It is always written as a colon `:` followed by a name. For example `p:hover`.

![image](https://github.com/gustavoalito/BeCode/assets/133368766/5ce6a00e-2561-4c5d-b685-d593d64586c3)

In the above code, whenever the mouse hovers over a paragraph element, that paragraph will have a lime-colored background.

## Specificity

Specificity is the order by which the browser decides which CSS styles will be displayed. A best practice in CSS is to style elements while using the lowest degree of specificity so that if an element needs a new style, it is easy to override.

IDs are the most specific selector in CSS, followed by classes, and finally, type. For example, consider the following HTML and CSS:

```
<h1 class='headline'>Breaking News</h1>
```

```
h1 {  color: red;} .headline {  color: firebrick;}
```

In the example code above, the color of the heading would be set to `firebrick`, as the class selector is more specific than the type selector. If an ID attribute (and selector) were added to the code above, the styles within the ID selector’s body would override all other styles for the heading.

Over time, as files grow with code, many elements may have IDs, which can make CSS difficult to edit since a new, more specific style must be created to change the style of an element.

To make styles easy to edit, it’s best to style with a type selector, if possible. If not, add a class selector. If that is not specific enough, then consider using an ID selector.

## Chaining

When writing CSS rules, it’s possible to require an HTML element to have two or more CSS [selectors](https://www.codecademy.com/resources/docs/css/selectors) at the same time.

This is done by combining multiple selectors, which we will refer to as chaining. For instance, if there was a `special` class for `<h1>` elements, the CSS would look like below:

```
h1.special { }
```

The code above would select only the `<h1>` elements with a class of `special`. If a `<p>` element also had a class of `special`, the rule in the example would not style the paragraph.

## Multiple Selectors

In order to make CSS more concise, it’s possible to add CSS styles to multiple CSS [selectors](https://www.codecademy.com/resources/docs/css/selectors) all at once. This prevents writing repetitive code.

For instance, the following code has repetitive style attributes:

```
h1 {  font-family: Georgia;} .menu {  font-family: Georgia;}
```

Instead of writing `font-family: Georgia` twice for two selectors, we can separate the selectors by a comma to apply the same style to both, like this:

```
h1, .menu {  font-family: Georgia;}
```

By separating the CSS selectors with a comma, both the `<h1>` elements and the elements with the `menu` class will receive the `font-family: Georgia` styling.


---

### Some good references:

- https://www.codecademy.com/resources/docs/css
- https://www.codecademy.com/workspaces (to practice on a template)



