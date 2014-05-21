# Installing Requirements
**Windows Users** - Please note that it is highly recommended that you first install [Cygwin](https://www.cygwin.com/install.html)
in order to follow along with Unix based commands.

1. Sign up for a free [Github](https://help.github.com/articles/signing-up-for-a-new-github-account) account.
2. Download and Install [Git](https://help.github.com/articles/set-up-git).
3. Add an [SSH Key](https://help.github.com/articles/generating-ssh-keys) to your Github account.
4. Sign up for AWS.

    Step-by-step Instructions:

    1.  Open a web browser.
    2.  Go to the URL [aws.amazon.com](http://aws.amazon.com/). The AWS home page appears, containing an eye-catching "Sign Up Now" button.
    3.  Click the "Sign Up Now" button. You are redirected to an account sign-in page.
    4.  Enter you e-mail address and select the radio button labelled, "I am a new user." The "Login Credentials" page, first of the sign-up form pages, appears.
    5.  Fill in the account form. This will look familiar to the billion people who have shopped online. You must supply information about the customer, various ways of contacting the customer, a captcha-style security check and agreement to terms and conditions.
    6.  Find your credit card and fill in the payment form.
    7.  Fill in the identity verification form. I received an automated message on my phone and had to type in a PIN displayed in the web browser. A confirmation page appears. I also received a "welcome" e-mail, but did not have to click on any activation link to make my account active.
    8.  Close the web browser.

5. Install [Python](https://www.python.org/downloads/) if it is not already installed. By default python comes
installed in **Mac OS X** and **Linux**.
6. Install [pip](http://pip.readthedocs.org/en/latest/installing.html) if it is not already installed.
7. Install [node](http://nodejs.org/download/).

    * Windows users - install the **.msi** Installer.
    * Mac OS X users - install the Universal (**.pkg**) Installer.
    * Linux users - visit this [link](https://github.com/joyent/node/wiki/Installing-Node.js-via-package-manager).

8. Install [MySQL](http://dev.mysql.com/downloads/mysql/).

    *Note: If you have a 64-bit computer, make sure that your python and mysql bit versions match.
    For example, if your python distribution is 32-bit, then your MySQL version should also be 32-bit.
    I recommend installing 64-bit versions of both python and MySQL if you have a 64-bit computer.*

    To check your python bit version, open up your terminal and type `python`:

    ```
    $ python
    ```

    You should now be within your python shell. You should see something resembling the following:

    ```
    Python 2.7.5 (default, Sep 12 2013, 21:33:34)
    [GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.0.68)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
    ```

    Now import `platform` and run `platform.architecture()`.

    ```
    >>> import platform
    >>> platform.architecture()
    ('64bit', '')
    >>>
    ```

    You should now see what bit version of python you have running.

    * [Windows]()
    * [Mac OS X]()
    * [Linux]()


