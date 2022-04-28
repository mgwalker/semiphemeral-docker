# Docker setup for [semiphemeral](https://semiphemeral.com)

I created this gizmo so I could have an isolated environment to run
Semiphemeral. At the time I created it, the Semiphemeral instructions said to
install it from pip, but that was grabbing an older version with a dependency
mismatch. This Dockerfile handles fetching the most recent version and doing all
the right dependency installs so you don't have to!

1. Follow [the instructions](https://semiphemeral.com) to setup a Twitter app
   and create OAuth tokens.
2. Clone this repo. Then create a directory in the root called `config`. This
   directory is where your Semiphemeral configuration and tweets archive will be
   stored.
   - Note: The archive created by Semiphemeral is not the same as the [official
     archive from Twitter](https://help.twitter.com/en/managing-your-account/how-to-download-your-twitter-archive).
     It contains less information. If you intend to delete all of your Twitter
     history, consider downloading an official archive first.
3. Run `docker compose up` to enter Semiphemeral configuration.
4. Open your browser to [http://localhost:8080](http://localhost:8080) and paste
   in the values you got from Twitter. The rest of the configuration is
   described on the Semiphemeral site.
5. When you're done, click save. You can now close your browser.
6. Run `docker compose run semiphemeral <command>` where `command` is one of the
   options listed at the top of [the instructions](https://semiphemeral.com),
   such as `fetch` or `delete`.