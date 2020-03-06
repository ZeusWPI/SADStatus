import urllib.request
import urllib.error

from .statusenum import Status

def status(service):
    if service.password is None:
        # Simply check for HTTP 200
        try:
            request = urllib.request.urlopen(service.url)
            if request.getcode() == 200:
                # It succeeded, everything is fine
                return Status.ONLINE
            elif request.getcode() == 401:
                # It requested an authentication
                return Status.UNAUTHORIZED
            else:
                # It didn't succeed
                return Status.BROKEN
        except urllib.error.HTTPError:
            # urllib likes to throw HTTPErrors, meaning it failed
            return Status.NO_LOGIN
        except Exception as e:
            # Anything else is broken
            return Status.BROKEN
    else:
        # Check if there is an auth
        try:
            request = urllib.request.urlopen(service.url)
            # If we can open it without basic auth, something is wrong
            if request.getcode() == 200:
                return Status.NO_LOGIN
        except urllib.error.HTTPError:
            # Ignore HTTPErrors, these are mostly 401 errors, which we want
            pass
        except Exception as e:
            # Anything else is broken
            return Status.BROKEN

        # Check if the username/password works
        try:
            # Setup the password manager
            passman = urllib.request.HTTPPasswordMgrWithDefaultRealm()
            passman.add_password(None, service.url, service.username, service.password)
            authhandler = urllib.request.HTTPBasicAuthHandler(passman)
            opener = urllib.request.build_opener(authhandler)
            urllib.request.install_opener(opener)
            try:
                pagehandle = urllib.request.urlopen(service.url)
                if pagehandle.getcode() == 200:
                    # The page now loaded succesfully
                    return Status.PROTECTED
                elif pagehandle.getcode() == 401:
                    # Still unauthorized, username or password must be incorrect
                    return Status.LOGIN_FAILED
                else:
                    # The page loading still failed
                    return Status.BROKEN
            except urllib.error.HTTPError:
                # Catch loose urllib errors
                return Status.LOGIN_FAILED
            except Exception as e:
                # Anything else is broken
                return Status.BROKEN
        except Exception as e:
            print(e)
            return Status.BROKEN
