# bypass-fb-block-website-algorithm-bug

# Overview

If your website is blocked by Facebook. It is very difficult to request Facebook to unlock your website (except you paid the money to FB to unlock Facebook customer service) even the block reason is the block algorithm bug.
You can use this Github repository to make your redirect website, the redirect website can dynamically redirect your website and bypass Facebook blocked URL check. 
If you build a static redirect website page, this redirect website also can show the target website title / description / preview image on the Facebook post.

Hope Facebook can fix the block URL algorithm bug one day!

# How To Use

1. Dynamic redirect target website
    1. Git clone this repository and set your repository to enable the Github page.
    2. Edit /docs/js/validate.js, add your website domain into validate_domain array.
    3. You can use below URL format to bypass Facebook URL block check:
       "https://{your GitHub page url}?url={your target URL with URL encode}"

2. Static redirect target website
    1. Git clone this repository and set your repository to enable the Github page.
    2. Run "generate-index-html.py" python script, the usage:
       python generate-index-html.py {target url} {target output file name}
    3. The output file is generated on /docs/redirect/{target output file name}
    4. You can use below url format to bypass Facebook url block check and it will show preview title / description / image:
       "https://{your github page url}/redirect/{target output file name}"

# Requirement for generate-index-html.py
  * urllib3>=1.25.6
  * bs4>=0.0.1
  * lxml>=4.5.1

# License
This project is licensed under the terms of the MIT license.