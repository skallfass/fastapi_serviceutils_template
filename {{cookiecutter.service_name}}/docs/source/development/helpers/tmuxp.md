# tmuxp

For a predefined development environment the `.tmuxp.yml` configuration can
be used to create a [Tmux](../../../references/index.html#tmux)-session
(using [Tmuxp](../../../references/index.html#tmuxp)) with a window including
three panels:

* one panel for **editing files**
* one panel **running the service**
* one panel **running the tests**

Run the following command to create the tmux-session:

```bash
    tmuxp load .
```

Inside the `.tmuxp.yml` you can set your local environment variables, too, if
required.
