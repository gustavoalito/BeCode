# Doc 📖 : SESSION - COOKIE

## Learning objectives

- Starting with PHP
	* Learn the syntax
  	* Understand difference between Sessions and Cookies
	* How to set and retrieve `$_SESSION` superglobal
	* How to set and retrieve `$_COOKIE` superglobal
	* Learn common security issues as XSS and CSRF
- To know where to search for PHP documentation

## Browser Persistent Data with PHP

Data persistence is the means of storing information for a prolonged period of time. We can make applications that are "user aware" by using that information to set user preferences or show use input. 

## Sessions

A **Session** is a term referring to a user's time browsing a web site. It's meant to represent the time between a user's first page view on a particular site, until the time that user is finished at that site. PHP offers us the ability work with _session variables_ which are available for the duration of a user's session.

* [Session Variables: `$_SESSION`](https://www.php.net/manual/en/reserved.variables.session.php)
* [session_start()](https://www.php.net/manual/en/function.session-start.php)
* [session_destroy()](https://www.php.net/manual/en/function.session-destroy.php)

It's impossible to know for sure when a user is done with a site. Instead, the session is terminated in one of two ways :

- The user closes the browser
- The session times out when a request has not been made within a certain amount of time (1440 sec by default).

Changing Session Timeout :
```php
// server should keep session data for AT LEAST 1 hour
ini_set('session.gc_maxlifetime', 3600);

// each client should remember their session id for EXACTLY 1 hour
session_set_cookie_params(3600);

session_start();
```
### ⚠️ Session vunerability : XSS

A lot of people will argue that using sessions is the correct way of storing information about the user. The reason a lot of people when asking this is that it's easy ! Although this argument is true, it's also easy for a hacker to gain access to the same session for cross site scripting.

Sessions are prone to **cross site scripting (XSS)** because the **sessions are accessible via JavaScript** (😱) and there is no good way to keep that from happening.

[Learn more about Cross Site Scripting (XSS)](https://owasp.org/www-community/attacks/Session_hijacking_attack)


## Cookies 🍪

A **cookie** is a piece of data sent from a website and stored on the user's computer by the user's web browser.

- Cookies can have an HTTP only flag set on them to make them only visible to the browser and no scripts on the site.
- Cookies have the ability to only be transmitted over HTTPS, which makes it even more secure.

The way we can use cookies is to store JSON that contains all information about the user, allowing the cookie to be stateless.

### Setting a Cookie 🍪

Here is a list of available properties. View more on [setcookie() documentation](https://www.php.net/setcookie)

- **name**: The name of the cookie. You can store cookies as an array by adding square brackets to the end of the name.

```php
// cookie values as array
setcookie('cookiename[]', 'value1');
setcookie('cookiename[]', 'value2');
```

- **value** : The value of the cookie. This value is stored on the clients computer. Values stored in a cookie are stored as **strings**.  _Do not store sensitive information_.

```php
// assuming the name is 'cookiename[]', retrieve array values
echo $_COOKIE['cookiename'][0];
echo $_COOKIE['cookiename'][1];

// will display
value1value2
```

- **expire (optional)**: _default = 0_

The time the cookie expires. This is a Unix timestamp, you'll most likely set this with the [`time()` function](https://www.php.net/manual/en/function.time.php) plus the number of seconds before you want it to expire. If set to 0, or omitted, the cookie will expire at the end of the session (when the browser closes).

```php
// set the cookie to expire in 30 days. 
// 60 seconds, multiplied by 60 minutes, multiplied by 24 hours, multiplied by 30 days
setcookie('cookiename', 'value', time()+60*60*24*30);

//set the cookie to expire with session
setcookie('cookiename', 'value', 0);
```

- **path (optional)**: _default = the current directory in which the cookie is being set._

The path on the server in which the cookie will be available on. If set to `/`, the cookie will be available within the entire domain. If set to `/foo/`, the cookie will only be available within the `/foo/` directory and all sub-directories such as `/foo/bar/` of domain.

- **domain (optional)**: _default = works for all subdomains as well_

The (sub)domain that the cookie is available to. _Older browsers may require a leading `.` to match all subdomains._


```php
// available to a single subdomain
setcookie('cookiename', 'value', 0, 'www.example.com');

// available to all subdomain
setcookie('cookiename', 'value', 0, '.example.com');
```

- **secure (optional)**: _default = FALSE_

Indicates that the cookie should only be transmitted over a secure HTTPS connection from the client. When set to TRUE, the cookie will only be set if a secure connection exists. On the server-side, it's on the programmer to send this kind of cookie only on secure connection (e.g. with respect to `$_SERVER["HTTPS"]`).

- **httponly (optional)**: _default = FALSE_

When TRUE the cookie will be made accessible only through the HTTP protocol. This means that the cookie won't be accessible by scripting languages, such as JavaScript. It has been suggested that this setting can effectively help to reduce identity theft through XSS attacks (although it is not supported by all browsers), but that claim is often disputed.

### Deleting a Cookie

To delete a cookie, we set the cookie to an empty string that expires in the past. Making sure to use the same path we used for the original cookie.

```php
// Where $_GET['delete'] is the name of the cookie
setcookie($_GET['delete'], "", time() - 3600, '/');
```
### ⚠️ Cookie vulnerability : CSRF

The downside of cookies is that they are prone to **cross-site request forgery (CSRF)**, which allows a hacker to trick the browser into providing the cookie by using a form or image that is hidden from the user.

Protecting against cross site request forgery has a few steps that require storing a token (e.g. with JSON Web Tokens) in the PHP session that you can also place in a hidden input field on all forms.
Then, on a form submission, you would compare the token in the session with the one that was submitted, to make sure that they're both the same before proceeding.

[Learn more about Cross Site Request Forgery (CSRF)](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)

