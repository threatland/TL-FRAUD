DISCLAIMER
This program is intended ONLY for testing your own sites. 
Any other use of this program is forbidden. 
The Author does not take responsibility for any improper use of the program. 

ABOUT MBA
This version of Sentry is labeled Sentry MBA,  i.e. Sentry 2.0 modded by Astaris.
My thanks go to Sentinel for making this wonderful program and for giving away for free the source code.

PROGRAM FEATURES
- Supports Ajax
- Full OCR support
- Supports Fixed Captcha OCR sites (like sites that use Strongbox for example) by an user configurable database
- Features a special "Acquire Images" engine that let the user extend the database for fixed captcha sites. Moreover a training page can be generated in order to train Tesseract for specific fonts.
A database which includes Strongbox and other sites is included.
- Supports HTTPS
- Supports Socks 4a/5
- Features an advanced configuration of all the engine stages by using special variables: in this way user is able to configure correclty the engine for very specialized cases.
- Supports fully configurable Keywords Capture (useful in order to get premium account details)
- Supports fully configurable Form JavaScript Redirect (useful to get the page where a premium account detail is shown)
- Supports multiple additional form redirects, i.e. MBA is able to call additional URLs in order to capture keys from multiple pages.
- Supports advanced custom Parsing Code
- Supports advanced special Keywords Matching Functions
- Features an advanced Proxy Analyzer which supports special cleaning and filtering functions, above all the proxy filtering by IpFilter.
An IpFilter tweaked for the use with Sentry is included.
- Other unique features that you must discover by yourself

LIST OF CHANGES
Version 1.4
- Added support for three fields bruteforcing. Now when you'll start a bruteforcer session, MBA will ask you how to map the bruteforcer fields to the  loaded wordlist. It works in this way:
The bruteforcer fields are called <USER>, <PASS> and <EMAIL>. Take note that even if the third field is called <EMAIL> it doesn't  need to be linked to an email!
Each word of the loaded wordlist is treated like field1:field2:field3, i.e. now each word in the wordlist can be either a single, double or triple word. It will be called anyway a combo since i like the word to be named combo :P
So from the start bruteforcer form you will be able to assign field 1 to either <USER>, <PASS> and <EMAIL>. Same rule applies to field2 or field3.
Finally take note that in basic mode you should always assign field1 to <USER> and field2 to <PASS>. If you need otherwise, then you must switch to master mode.
- POST Wizard is now called Master Wizard. Here the main changes/additions:
1) For all the HTTP stages (except for the OCR one) user can set the call method: Head, Get, Post, Post MultiForm, Post Json. Take note that for the new POST methods you must format the POST data in the usual way...MBA will change the format
automatically once the POST data is built. Moreover for Json if you need to add a multivalue parameter just add \s at the end of the name parameter. In order to close a multiparameters section, add \e at the end of the name of the last parameter
of the section. Sections left open will be closed automatically, so no need to add \e to the last parameters.
2) Improved the default parsing engine, that now is fully three fields compatible. So now you can tell the default parser how many bruteforcer fields you expect from the form. For this you must use the indexes near each field. See context help for more detail.
3) Added Debugger available from the POST Wizard. In this way you can check for example all the forms and fields captured and debug any config error quickly. A debugger is available from OCR Wizard too.
4) Now you can parse form data from the Intermediate action ("From IA" option). Useful for sites for which the login page is actually called in the second stage.
5) You can enable/disable follow redirect for Intermediate action and redirect URL. Take note that a redirect to another domain will not be followed and will trigger instead an IP ban.
6) Now you can set mutiple redirect keys (and you can tell MBA if a key has to be a source key or a header key) and you can build them with the keyword wizard.
- Improved the parsing code engine. Her the main  changes/additions:
1) Now the function premium date is only one, but it is in fact a universal date converter. It will recognize automatically unixtime, days remaining format and (year, month, week, minute, hour, second) format. Only action user has to take it is when the premium date is given in
seconds remaining. In this case just add "second" as prefix or suffix.
2) Added user and pass functions. If a data extracted is marked as user or pass it will be added in the columns user and pass of the history.
3) Now you can set recursive option and capture target option for each field.
4) You can add mutiple fields even if parsing code is not used for capture or post fields extraction. This means that you can add multiple fields extraction when parsing code is used as a variable input.
In this case all fields captured will be just joined. But you will get a nice feature if you enable recursive parsing code from variable wizard. In this case each field captured mutiple times will
generate a vector of size equal to the number of times the parsing code has matched the field parsing strings. 
For example let's suppose you have a parsing code which captures fields field1 and field2.
field1 is captured 4 fimes with values field1_1, field1_2, field1_3, field1_4.
field2 is captured 1 time with value field2_1.
You will get a vector Key[] of size 4 with these values:
Key[1] = field1_1field2_1
Key[2] = field1_2field2_1
Key[3] = field1_3field2_1
Key[4] = field1_4field2_1
What to do with this vector? Well when you have computed a variable in such way, you can do only one thing with the var...Assign it to an additional redirect paameter (be it POST or URL)...the additional redirect URL will be called in this case four times, each time with
the assigned value corresponding to the index assigned, i.e. first time MBA will use Key[1], second time Key[2] and so on.
5) Added Pefix and Suffix inputs. They will be added right before and after the data extracted. In chain mode with these ones filled, you can get almost all work done with just one variable :)
- Improved the variables engine:
1) Added new crypto functions (RSA and HMAC) and all SHA hash methods, plus other convert and string functions.
2) Now variables supports mutiinput functions. In order to configure such functions, new functions have been added, SetParameterIndex and SetParameterValue, see context help for more details.
3) Now you can re-assign an already computed variable with the new function SetField. With this one you can also set the user, pass and email of the combo being tested. The captcha too can be reasiigned.
This feature together with the new variable flow control options will give the user the chance to excecute different variables codes as a function of the server response.
4) Now you can assign the header too to any stage. Mutiple headers can be assigned if you use \n as fields separator. Fields already present will be replaced.
5) Added OCR stage. In this way you can manipulate captcha code right after the image is recognized.
6) Added loop variables. Thiese variables will set the enry point of a loop cycle that can be triggered by the new Jump function.
7) You can add additional redirect URLs by variables. This will let you to add such URLs recursively based on the response got from the last additional redirect URL.
- Totally rewritten the HTTP debugger.Go to check, too lazy to explain the details here.
- In Keywords Wizard you can set keys for Intermediate action only. Moreover fake image ban key has been added.
- Other major and minor improvements/additions here and there.
- Solved critical, major and minor bugs.
Finally new languages from cp20 to cp26 (excluded cp21...) have been added. Thanx go to Jenva/Atterdale and machak :)

Version 1.3.4c
- Added new option in Fakes Settings frame to enable keywords engine on Intermediate Action stage.
- Added remove duplicates function in wordlist frame. After removing duplicates, user must save wordlist before it can be used in the bruteforcer.
- In all URLs and Post fields from Post Wizard <USER>, <PASS> and <Captcha> will be replaced with the user and pass of the combo being tested and with the OCR code of the recoginzed image, if any.
- Now both good users and combo expired will be added to the Users/Combo tab in progression frame.
- Wordlist position will be saved based on the file fingerprint computed directly on the file content: in this way position will be rembered even if user changes filename.
- If the same wordlist is used by multiple brutefrocers, it is shared at progression frame level in order to optimize memory usage.
- From the history options frame user can tell MBA what types of progression results must be sent automatically to the history.
- Solved two critical bugs that would lead to an out of memory error.
- Solved a major memory leak in history analyzer. Moreover loading time of history bots has been improved.
- Solved a major bug in hisotry frame that would cause the hits obtained with separate lists to be deleted at the program start.
Finally two new Tess languages have been added...thanx to Jenva22/Atterdale as always :)

Version 1.3.4b1
- Now the bot debug is trimmed to 2MB before copying it to the memory: this should solve i hope the out of memory error some users are having.
- Now for each stage, the maximum number of HTTP redirects followed has been limited to 10: this should prevent an infinite redirect loop caused by shitty proxies.

Version 1.3.4b
- Now in History frame you can filter list by site name.
- Added new key type in advanced keyword mode -> ban key type.
  There are four types atm:
  - Normal -> Legacy ban key
  - Conditional Ban -> if such key is matched, then MBA will restart authentication process with same proxy but wrong combo. If MBA get a bad login response with wrong combo (i.e. fail key is matched), then the original combo will be marked as bad,
    if the ban key is matched istead, then the proxy will be banned and the combo will be retried with another proxy. This type of key is useful for sites where the banned response and the one for banned combos (i.e. shared accounts) are the same.
 - Login Page Ban -> This key will trigger an IP ban ONLY if it is matched against the login page.
 - Black List Ban -> If such key is matched the proxy will be banned AND added to the blacklist.
- Added a new option in keywords wizard -> Require Empty Body. If such option is cheched, then a header key will be matched ONLY if the body sent together with the headers is empty. Useful for Ajax sites that send fail login response over an empty body.
- Added new option in fakes settings frame -> Process error codes. If this option is checked, ALL http error codes (excluded of course TCP socket errors, that in fact are no HTTP errors, well just to be clear :P) will be processed by the keyword engine, i.e.
  you will be able to match for example a not found code in the HTTP headers.
- Added another option in fakes settings frame -> Bad Path Detection. This one was a feature already available before, but now you can disable it, that's the difference :P
- Now in Post Wizard you can tell MBA to authenticate with basic authentication field, i.e. you'll be able to bruteforce popup sites with the same engine activated for form sites. What's the advantage? Well, you can capture all the fu*k you want, simple :D
  So i should really change the name from Post Wizard to something else, any idea? :P
- The keyword engine for basic popup sites now searches for header keys also on 401 headers. What's the advantage? Simple, you can identify really bad proxies based on the authentication realm field, that's a hint :D
- Now in the proxy analyzer frame you can remove all the proxies that are no more in the proxy list: this is useful to better synchronyze the analyzer after you found with bruteforcing that some proxies really suck :P
- Various improvements in the bruteforcer engine.
- Solved major and minor bugs here and there.
And finally I added 7 new Tess language. You already know the man you must thank for this: congrats to Jenva22 aka Atterdale aka The captcha Killer :P
Ok maybe i forgot something, so lemme add only Happy New Year  (HNY and btw RTFRN, RTFF and RTFB!) and please don't believe to all the shit surrounding this number :D

Version 1.3.4a
- Improved parsing code engine: now it is faster and has better memory usage. Moreover a critical bug has been fixed.
- Fixed a critical bug that would lead to the program freeze when banning window is activated and a certain codition is met.
- Prevented a critical condtion that would lead to an out of memory error when unexpected large data (> 6 MB) is downloaded by a bot. For this reason now all data is trimmed to 2 MB on HTTP level.
- Fixed a minor bug that would cause a combo to be assigned to two different bots.
- The maximum number of users you can store in the users tab is limited from now on to 1000 for each site. Moreover HTML sources and bot debug information are not stored
  in this tab. This is to prevent an out of memory error when a really large number of users is captured. Don't worry, all users will be saved at the end of the bruteforce
 session even if they don't appear in this tab.
- Now the debug.txt is kept in the memory for better performance. It will be written and shown under user request by clicking on the proper button from the progression frame.
  For this reason the option is not more in the general settings frame. File limit is still set to 10 MB.
- Added new option in general settings frame that will help users with performance problems.
- Now you can mark a failure key as expired account in advanced mode. Such combos will be saved at the end of the bruteforce session.
- Fixed 1 critical bug and 2 major bugs in the OCR extraction engine.
- Improved the subextraction filter in OCR engine.
- Added new options in OCR wizard -> check them out :P
Finally 2 more languages for Tess have been added -> cp5 and cp6. They are like cp10, but cp5 is a full language set, while cp6 includes only digits and upper letters.
Thanx again to Jenva22 :)

Version 1.3.4
First thing, this version comes with new language packs for Tesseract: cp4, cp7, cp8, cp9 and cp10. From now on, if you want to check
for which captcha a language is for, you must download language samples, available as separate download.
But i must thank and congratulate Jenva22 who gives me an improved cp1, an improved cp4 and finally cp10: with these ones you can get
around 80% recognition rate at very fast speed on some not so easy captcha. So you must give credits to Jenva22 for these ones :)
And now let's go with the changes:
- Added a very major feature: annoying sound on hit, no need to explain this one i guess and you must thank user zero for this one, he kept annoyng me
at vey fast rate until i implemented this one, so kudos to zero :)
- Improved proxy analyzer engine:
1) Now in the options form you can select and create judge profiles. A judge profile tells MBA which key have to be on the judge answer and how to parse gateway and
annon level string. In short now each judge on earth is supported :P
2) Improved internal judge: the judge will tell you if a proxy is detected as such, i.e. you'll be able to differentiate between high anonymous and anonymous proxies.
3) Now the analyzer will tell you the country of the proxy/socks.
4) You can skip judge test on proxies already checked: in this way proxy test against a site and/or https test will be much faster for already judged proxies.
5) Other additions that you must discover by yourself since my lazyness has reached its limit on this line :P
- Separate lists support -> from the wordlist frame you can now select three operating modes: Legacy Mode, Separate Lists Mode 0 and Separate Lists Mode 1.
- Now you can tell MBA to save good usernames on a file. A good username is a username that is in the server database, but the combo associated is marked by MBA as bad since the pass is wrong.
You can tell MBA to mark such combos as good usernames combos by adding a fail key in advanced mode and selecting proper key type. Moreover good usernames will go in the new users tab.
- You can mark also keys as bad usernames: in this way a combo with a bad username in it will be not retried.
- Global keys now support header/source ban and retry keys. The global key is added by default as a global sorce retry key. By adding the key in advanced mode,
you can set the key to other types listed above. For this reason file for global keys has been changed, so use the new one available with this version.
- Database has been improved: now it operates in two different ways and the best mode is selected automatically based on the type of image downloaded.
For this reason you must use the new database available in this version. Moreover the database update engine has been moved to a separate thread
and you'll be able to see the update progress from a crappy gui :P
- You can set a key captured as credit type: in this way the data captured will go in the new column credits in the history frame. Anyway take into account that
the data captured need to be a number, so no letters or shit chars allowed. It supports anyway decimal separator (both '.' and ',').
- Overall redesign of frames controls...you will see :)
- Minor additions here and there.
- Minor improvements here and there
- Critical, major and minor bug fixes here and there.

Version 1.3.3c
- Ok, I found a way to minimize graphic corruption under Vista/Seven without the need of frame refreshing. This means two things:
 1) Now Windows Vista/Seven refresh mode is disabled by default.
 2) No more flickering.
- In last version i completely broken email saving...sorry guys i was a little tired and i had too much beer the day before :P
- Fixed some mispelling and wrong format for keys captured under Parsing code wizard (Thanx Arden)

Version 1.3.3b
- Changed the timeout engine from a timer based one to a thread based one: this should solve some issues on certain systems.
- Improved the aborting engine for both the bruteforcer and proxy analyzer: now when a bot is hard aborted it should be freed without any problems on any systems :P
- In the proxy analyzer if site analysis is enabled, the engine shows in greater detail the site check result.
- In the proxy analyzer when options are changed, the changes are applied upon form close (i.e. as soon as the user click on use data button) -> no need to switch frame.
- Now if a problem arises when loading history file, the save function is disabled. In this way there's no risk to overwrite the file with an empty one. Same behaviour applies to global source keys file.
- Solved minor graphic corruption issues in keywords frame and wordlist frame.
- In wordlist frame now there are the box to load separate username and password files -> there is only the gui, no active code -> full support in next version.
- Minor improvements here and there
- Minor bug fixes here and there.

Version 1.3.3a
- Added computational OCR option in OCR Wizard: MBA will try to get a result from an image that is actually an algebric operation.
- Added two new columns in history frame: Emal and Premium.
  1) MBA will automatically recognize an email from captured keys and add it to the colums email. Take note that MBA will not extract emails from a string captured -> it will just check if the string it is an email. So be sure to capture just the email with a parsing string, i.e. no html tags or other shit is allowed :P
  2) If you define a key in parsing code wizard as a date in custom functions menu, then this date will be added in the premium colums of the history frame. If you have an old snapshot and you want this feature to work, it is enough that you open the parsing code wizard and set the key that captures the premium date to (surprise surprise) premium date :P
      If the key is already set to unix date or mega date, then this new feature will work automatically.
- Added new saving options in history frame. Go check them you lazy crackers :P
- Solved a serious memory leak in OCR engine that would lead after sometime to a thread creation error.
- Minor improvements here and there.
- Major and minor bug fixes here and there.

Version 1.3.3 (Final)
- Additional redirect URLs configuration by variables was broken in previous beta -> fixed.
- Now files browsing should work without performance issues under XP too.

Version 1.3.3 BETA 4
- Fixed crirical bug in OCR Wizard that would cause corruption in the shown  processed image.
- Fixed major bug in History frame that would cause an out of bounds error when saving the hits to a file.
- Fixed critical bug that would cause under certain conditions MBA to close without messages when browsing for a file with OCR engine active.
- Improved multithreading engine: now there are less threads managed with a simple dispatcher engine: so around same performance and better memory usage.
- Added new option in Fake Settings Frame that let the user disable (for form sites only) the default follow redirects method: i.e. the user can now force MBA to follow redirects at bot level -> this means that before following a redirect, header keys are checked and ONLY if not match is found THEN the redirect is followed.
- Now OCR stage engine can be set after Intermediate Action Stage. If you enable this feature, for now you must configure Image URL by variables.
- Now MBA should detect if there are any problem with Tess.dll and help the user locate the problem when such errors arise while user try to recognize an image in Tesseract mode.
Moreover added a new language for Tesseract. To check each language for which captcha is for, look in the directory Image Language Samples.

Version 1.3.3 BETA 3
- Fixed major and minor bugs here and there.
Moreover:
- Added new Tesseract language cp2 that allows a recognition rate around 97% for 21sextury captcha.
- Added new captcha to image database, see sample 5 in images database samples dir (big thanx to robdrobd, Jdogzz and Protektor).

Version 1.3.3 BETA 2
- Fixed major and minor bugs here and there.

Version 1.3.3 BETA
- Now MBA supports multiple sites bruteforcing.
- Improved multithreading engine
- Improved Tesseract behaviour: now the recognition rate remains stable across a large number of images on all capthca...previously it would decrease with certain capthca.
- Now right string in custom parsing code supports jolly char '*'. This feature together with new option maximum right string length will allow for some really powerful data capture.
- Added multiple options in fake settings frame, too lazy to enumerate them here...see by yourself :P
- Solved critical bug in database mode.
- Solved critical bug in the cookie engine.
- Minor improvements here and there.
- Minor and major bug fixes here and there.

Version 1.3.2
- Added additional redirect feature: now from variables wizard you can add how many additional redirect URLs you want -> from each page got, MBA will capture data definied in the Capture Stage. See context help for details.
- Improved image URL parsing by variables: now if you link the Image URL to a variable, the variable settings will be used by OCR Wizard. This is useful for some sites that define the captcha URL by javascript -> in these cases only way to get the image URL is to use variables.
- Now in varables wizard you can define conditional variables, i.e. variables that are not needed to compete successfully the authentication process.
- From now on, only one istance of MBA will be available...i know that this will upset some of you boys and girls (there are girls too, right? :P), but fact is that atm MBA doesn't support multiple istances, but do not worry, multi site cracking will be implemented, so only one istance you'll need!
- Now you can send a proxy/sock to the http debugger from the progression frame
- Changed a little how the Hits are saved: from now on only the results with a success key match will go in the "Hit Tab", the ones got from the afterfingerprinting engine will go to the "To Check" Tab and WILL NOT automatically saved in history. 
  So better you check these results to check...i reccomend you to check the source by right click -> view source answer in browser, in this way you can properly update success keys.
- Now Afterfingerprint can be disabled for form sites too.
- Removed two options for the basic auth engine ("check hit with another proxy" and "check meta redirect"), since with the new engine these options were useless, well at least i never used them :P
- Solved a majorl bug triggered under certain conditions when socks are used
- Mnor bug fixes here and there

Version 1.3.1b
- Solved critical bug that caused a sudden program crash on certain sites with follow redirect enabled (well actually this bug was triggered by 1 site...thanx to machak110 for reporting) 
- Solved a memory leak in the custom parsing engine
- Added URL encoding pass to data captured with parsing code when the value extracted has to be posted

Version 1.3.1a
- Finally fixed a critical bug in the HTTP library triggered randomly when bruteforcing HTTPS sites with SSL proxies. I tested various sites and now SSL works beatifully. Anyway if you experience other bugs, please report to me.
- Fixed a bug in the History engine (thanx to machak110 for reporting)
- Fixed a bug in the URL syntax checking engine (again thanx to machak110 for reporting)

Version 1.3.1
- Now MBA is able to process animated gifs with Tesseract.
- Improved the combo filtering engine by adding new options.
- Improved the parsing code: now you can use recursive mode in order to capture multiple strings with one parsing string -> ideal for capture table data.
- Left string in parsing code now supports jolly char * that matches any string. In this way you're able to capture data when the left string generated by parsing code wizard contains variable data.
- Introduced conditional OCR: you can activate the OCR engine only when a user configurable string is matched against the source page -> ideal for sites that requires a captcha after a certain number of failed attampts.
. Improved the form engine.
- Moved to separate threads several engines to improve performance and stability.
- Solved major and minor bugs here and there.

Version 1.3.0
- Solved two major bugs in the HTTP library: now https proxies work as expected and socks behaviour is improved.
- Now HTTPS proxies are enabled by default. Anyway if you experience abnormal program behaviour with https proxies enabled when bruteforcing https sites, you can always disable them from the proxies settings frame.
- Now the proxies analyzer is able to check socks too.
- Solved critical, major and minor bugs here and there.

Version 1.3.0 BETA
- Introduced HTTPS support. MBA supports HTTPS by direct connection or by socks. ATM for a bug in the HTTP libraries, HTTPS proxies are not supported,
  anyway you can force the use of such proxies by enabling them in the proxies settings frame.
- Now MBA supports socks level 4 (they must be 4a) and level 5. You can use socks with both HTTP and HTTPS protocols. If you want to import socks in the proxies list,
  you must select load socks (you must specify level) from the Proxy List settings frame. You can of course import socks from the clipboard too.
- Improved the Variables Wizard with new functions added.
- Improved the capture engine: the keys will be captured on both the post answer and the form redirect answer.
- Improved the Form Redirect URL: now the redirect condition will be matched against headers too.
- You can now view the received headers in your default text editiors by right clicking on a URL in the progression frame and selecting the appropriate option.
- You can copy to clipboard the Redirect URL of a redirect result by right clicking on the URL in the progression frame and selecting the appropriate option
- The Save filter has been improved: i suggest you to use as new filter string the following one:
  Keys captured:\n-------------\n<KEYS>\n-------------\nCookie received: <COOKIE>\n
- Solved major and minor bugs here and there


Version 1.2.9a.1
- Improved Waiting Window behaviour
- Now when a form redirect is triggered, the negine automatically recognizes if it has to follow true redirects, i.e. 3xx header codes.

Version 1.2.9
- Introduces Variables Wizard, a new wizard that can be launched from the Post Wizard. From here you can create Ajax variables in order to defeat some strong Ajax sites out there.
- Now you can use in both Parsing Code Wizard and Keyword Wizard safely characters reserved for string formatting, i.e. "|", "&" and ";". This chars will automatically replaced by their ASCII codes.
- Now in the general settings frame you can set 0  (new default) in the delay between each bot relaunch.
- Improved Snapshot engine.
- Fixed critical, major and minor bugs here and there.
- Updated Image database for several sites -> big thanks to johnmaxwell and jenva22

Version 1.2.8d
- Now all the combo related settings are in the general settings frame. Added two new options to the combo filter: you can now filter combo containing a defined set of characters and can force for each combo the password to be equal to the username.
- When a combo list is loaded, for all rows without the separator (:), the password will be set equal to the username.
- Improved the cookie engine for sites that, before sending the login page, send a chain of redirects for ajax script initialization.
- Improved the HTML tags checker.

Version 1.2.8c
- Added Image Blending option to OCR Wizard:enable this option if the capthca image is made of two images, one that acts as a background image and a top image that blends over the background image.
- Added Tesseract offline testing: in this mode all images in the selected directory will be processed with the current OCR Wizard processing options and the OCR Recognition Rate will be computed. This is useful for quickly tweaking processing options. You need to put in a directory all the captcha images renamed with the capthca code. You can use the acquire engine to save the capctha images. In order to have a good Recognition Rate evaluation use at least 100 images.
- Added new option "Source Tags Checker" in Fake Settings Frame: if this option is enabled, the engine accuracy with respect to false positives will greatly increase, especially for real time OCR from sites, where the afterprint engine is disabled from version 1.2.8 for speed reasons.
- Fixed a minor bug in OCR Wizard.

Version 1.2.8b
- Solved critical bug in extract characters procedure

Version 1.2.8
- Added a lot of new options in the OCR Wizard, such as Line Remover, Adaptive Invert, Characters SubExtraction and...well check for yourself :)
- Now you can tell Sentry to not update the Image URL: this should improve bruteforcing speed for some sites that use static image URL.
- When refresh cookie is selected and no data are needed from the login page, now the bot will return as soon as the cookie is updated: another feature to improve bruteforcing speed.
- Now the parsing engine recognize correctly not visible fields marked as input fields: this fields will be marked instead as hidden.
- Now you can copy in forum format hits from the histry frame: useful for all lazy crachers out there...
- Solved critical bug in OCR WIzard.
- Solved major bugs in Parsing Code Wizard and Keyword engine.
- Solved minor bugs here and there.

Version 1.2.7.b
- Now you can set color tolerance individually of each color to remove in second stage of Image Processing engine
- Tolerance option extended to third stage colors too
- You can enable fonts horizontal reconstruction in third stage
- Solved major bugs in Form Parser engine
- Minor bug fixes here and there

Version 1.2.7
- Added new tolerance option in OCR Wizard useful to remove with greater effectiveness unwanted background colors from captcha image
- Now you can download the image from the OCR Wizard with a proxy chosen from the proxy list loaded in Sentry.
- You can update in real time the keywords that the Briteforcer is using by clicking on the new Update button available from the keywords settings frame
- You can set a retry key as bad ocr code type in order to get realtime statistic showing the recognition rate of capthca images while bruteforcing
- Now the refresh data option in post wizard refreshes login and password fields too
- Solved a major bug in OCR engine by upgrading the mutithreading management of OCR threads
- Solved minor bugs here and there
- Updated the image database for fixed captcha sites (thanks johnmaxwell and jenva22)

Version 1.2.6b
- Solved three major bugs in the OCR engine

Version 1.2.6
- Changed the Snaphot Format: now all the keywords are saved in the main snapshot file (<site_domain>.ini in SnapShots directory). In this way it's more easy for users to share their profiles.
  In order to convert a snaphot form a previous version to the new format follow carefully these steps:
  1) From the general settings frame, click on the button load snapshot, browse to snapshot directory and select the file you want to convert.
  2) You will be prompted to enter the member URL of the site: enter the member URL exactly as it appears in Sentry Site text box.
  3) Click on the button save snapshot
- Changed the resize filter in the OCR engine since the previous one was not good for Tesseract
- Changed the resolution steps of the resize filter: a resize value of 1 will get the image resized to 110%, 2 to 120% and so on. So for example in order to rezize the image to 2X, enter 10 (200 %).
- Added a new function in OCR Wizard: Training Mode for the Acquire engine. This feauture let the user generate a training page in tif format for training Tesseract. Experimental!
- Now the OCR Wizard scan for all Tesseract languages installed in Tessdata directory and let the user select the language that Tesseract will use for image recognize.
- Added a new option in Fake Settings frame: Ban Proxy on empty source -> by enabling this option, the engine will ban proxies that receive an empty body for the site under attack: useful for some sites that keep sending empty HTML sources when they ban a proxy.
- Solved some minor bugs.

Version 1.2.5
- Added new option in OCR Wizard: now you remove with two different options colors form background and colors form the fonts. In the second case, the processing engine will try to reconstruct the characters after removing the selected colors.
- Added new option in the last stage of OCR Wizard that allows to convert to lower case or upper case the OCR output string.
- Solved some minor bugs.

Version 1.2.4
- Added Reconstruct option to OCR engine: if this option is disabled, the processing engine will not reconstruct the capthca characters after removing the colors you selected in second stage.
- Added Pixel Info text box to OCR Wizard: the box shows the user the pixel color properties when the user moves the mouse pointer around the image process box: this should help configure the processing options.
- Added UpDown buttons to increase/decrease each numeric value in the image processing options.
- Solved a bug that would keep removing colors added to the Combo menu in second stage options even if the remove color option was disabled.

Version 1.2.3
- Added Blur option to the OCR engine, useful to remove noise from the captcha image.
- Added Remove colors option to the OCR engine, useful to remove lines that overlap the captcha Fonts.
- Now the OCR engine saturation option allow to desaturate colors with negative values, useful to decrease luminosity of unwanted object from the captcha image.
- Improved the OCR characters extraction algorithm with new options.
- Added string filter feature to the OCR engine.
- Improved a lot of code in the OCR multithreading engine.

Version 1.2.2
- Improved the OCR engine multithreading
- Solved a bug that would cause an OCR Thread to keep busy Tesseract when the processing engine does not recognize the image format
- SOlved a bug introduced in previous version that would keep the Abort button in the OCR Wizard disabled even after pressing the Start button
- Extended the image database to some Strongbox sites that use a little different format for the captcha images

Version 1.2.1
- Now the OCR engine (image processing + tesseract) is a fully multithreaded engine. This means that the main thread (i.e. the GUI) is not slowed down while bruteforcing Captcha sites.
- Added context help to all the image preprocessing options in the OCR Wizard.
- Improved performance and accuracy on the extact + rotate image preprocessing options. Some work has still to be done in this area.
- Solved a bug that would cause the OCR WIzard to stop responding in certain conditions.
- Solved a bug that would cause an incorrect parsing of the Image URL in certain conditions.

Version 1.2
- Added full OCR support with Tesseract integration. This feature is still an early implementation, so expect some bugs. More options will be added later.
- Changed Parsing Code Wizard and OCR Wizard interfaces.
- Added new option to Parsing Code Wizard: now you can send to intermediate action too the data retrieved from login page with custom parsing.
- Fixed a bug in the parsing code that would prevent to extract correcly images URLS when special characters (\t and \n) are used.

Version 1.1.03
- Changed the images database engine algorithm: now it is a little faster and more accurate. Replace the ImageData.dat with the new one!
- Improved the image URL parsing
- Fixed a bug that would prevent the OCR from recognizing some captcha.
- Now the images acquiring engine that can be launched from the OCR Wizard is able to automatically detect fixed captcha sites: the Status text box becomes green when such a site i detected.
Finally the Image database has been extended by adding some missing strongbox images (from the latest version).

Version 1.1.02
- Added new database function available from the general settings frame: by clicking on the button "Update Images Database From File" you
can update your own database from another user database. In this way users can exchange individual database upgrades.
- Fixed some bugs here and there (i totally forgot which ones i fixed...)

Version 1.1.01
- Now the OCR Wizard shows correctly animated gifs
- Solved some minor bugs in the Keywords Frame and in the OCR Wizard form

Version 1.1
- Added support for Strongbox and other "Fixed Captcha" sites. The OCR engine for these sites is based on the database file ImageData.dat.
  Support for other sites that use fixed captcha images but not included in the database can be added by the user thanks to an image acquiring engine and
   to a built in function able to update the database with a single button click.
- All OCR settings can be configured by launching the new "OCR Wizard" available from the "Post Wizard".
- Improved the Keyword Engine: now you can configure special key matching functions by launching the new" Keyword Wizard" available from the Keywords Frame.
- Improved the Proxy Analyzer Engine: now the engine is a full 3 levels stage engine. Moreover you can filter the proxy list by using the included IpFilter.dat.
  The users can also modify the IpFilter.dat to better suit their preferences: the only constraint is the file format, that must be "Emule style" format.
- Updated the core components to the last versions.
- The program now looks correctly under Windows Vista/Seven, except for really minor glitches.
- The Proxylist and the HistoryList are dynamically updated when the Bruteforcer is running. 
  Moreover all the changes you make in the Proxylist are transferred in real time to the Bruteforcer.
- Changed the GUI to my tastes: i hope you like it! Thank you Claudia for the awesome pictures!
- Major improvements to the form and basic engines.
- Added new minor functions here and there: try the program and discover for yourself ;)

Version 1.03
- Now you can build your own Parsing Code by using the new Parsing Code Wizard, available from the Posting Wizard. For details see included help.
- The History List has two new columns: Captured Keys and Received Cookie. Moreover by right clicking on a site in the list you can copy the Cookie to the clipboard.
- The save filter in the History Options can accept the new variables <Keys> and <Cookie>.
- Now Sentry validates the syntax of the user settings in each frame. An error is issued if the syntax is wrong.
- The Custom Parsing Code Engine has been improved: now it's possible to set the fields to capture independently from the order they appear in the HTML source.  
- The Default Parsing Code Engine has been improved too: now it captures correctly the form fields on all sites (based on my neverending tests...) that do not generate the form object by javascript.   

Version 1.02
- Bug Fixes here and there 

Version 1.01
- Bug Fixes here and there 

Version 1.0
First MBA version. See included "Sentry_MBA_Help.pdf" for details.