## What

Given input raw string (even with backslash escaped double quotes), output
new string with every character in the string prepended with the &#818;
HTML escape code "combining low line", which more or less ends up looking
like underlined text.

#### Given 
```
r""""You need a 2\"x3\" """
```

#### Output

```
&#818;"&#818;Y&#818;o&#818;u&#818; &#818;n&#818;e&#818;e&#818;d&#818; &#818;a&#818; &#818;2&#818;\\&#818;"&#818;x&#818;3&#818;\\&#818;"
```

When put into a Markdown document (like this README), it renders thusly:  

&#818;"&#818;Y&#818;o&#818;u&#818; &#818;n&#818;e&#818;e&#818;d&#818; &#818;a&#818; &#818;2&#818;\\&#818;"&#818;x&#818;3&#818;\\&#818;"

