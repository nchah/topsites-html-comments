# topsites-html-comments
A script to create a collection of the comments left in the HTML code of various high traffic sites as ranked by Alexa.com. A search for easter eggs, if there are any.


## Background ##
Further background in https://blog.nielchah.com/2016/01/05/top-sites-html-comments/


## Brief Description ##

### topsites.txt ###
A newline separated file of the 500 top sites as ranked by Alexa.com.

### topsites-comments.json ###
A JSON file loaded with data on the first 2 topsites.


## Command Line ##
It can now be run on the command line. 

    $ python3 topsites-comments.py --site=http://mozilla.org
    Request Sent.
    Getting HTML comments.
    
    COMMENT #1/18:
                 _.-~-.
               7''  Q..\
            _7         (_
          _7  _/    _q.  /
        _7 . ___  /VVvv-'_                                            .
       7/ / /~- \_\\      '-._     .-'                      /       //
      ./ ( /-~-/||'=.__  '::. '-~'' {             ___   /  //     ./{
     V   V-~-~| ||   __''_   ':::.   ''~-~.___.-'' _/  // / {_   /  {  /
      VV/-~-~-|/ \ .'__'. '.    '::                     _ _ _        ''.
      / /~~~~||VVV/ /  \ )  \        _ __ ___   ___ ___(_) | | __ _   .::'
     / (~-~-~\\.-' /    \'   \::::. | '_ ` _ \ / _ \_  / | | |/ _` | :::'
    /..\    /..\__/      '     '::: | | | | | | (_) / /| | | | (_| | ::'
    vVVv    vVVv                 ': |_| |_| |_|\___/___|_|_|_|\__,_| ''
    
    Hi there, nice to meet you!
    
    Interested in having a direct impact on hundreds of millions of users? Join
    Mozilla, and become part of a global community that’s helping to build a
    brighter future for the Web.
    
    Visit https://careers.mozilla.org to learn about our current job openings.
    Visit https://www.mozilla.org/contribute for more ways to get involved and
    help support Mozilla.
    
    ...


    $ python3 topsites-comments.py --site=http://amazon.com
    Request Sent.
    Getting HTML comments.

    COMMENT #1/21: [if lt IE 7]><html class="a-no-js a-lt-ie10 a-lt-ie9 a-lt-ie8 a-lt-ie7 a-ie6" data-19ax5a9jf="dingo"><![endif]

    COMMENT #2/21: [if IE 7]><html class="a-no-js a-lt-ie10 a-lt-ie9 a-lt-ie8 a-ie7" data-19ax5a9jf="dingo"><![endif]

    ...

    COMMENT #10/21:  ==============================================

    Could our homepage be better? Interested in building it?
    http://www.amazon.jobs/jobs/349033/software-development-engineer
    
    ===============================================
    
    ...


## License ##
This code is released under the MIT License.


