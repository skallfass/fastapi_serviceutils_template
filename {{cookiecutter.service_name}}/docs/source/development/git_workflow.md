# Git-workflow

The git workflow used in development of this service is oriented on:
[a stable mainline branching model for git](http://www.bitsnbites.eu/a-stable-mainline-branching-model-for-git/)

Each new feature, bugfix, endpoint, etc. results in a new `feature-branch`.

To create such a feature-branch run the following:

Ensure the `devl-branch` is up to date:
```bash
    git checkout devl
    git pull
```

Then create the `feature-branch`:
```bash
    git checkout -b <feature_branch_name>
```

Now we develop inside this new `feature-branch` on our new feature.

!!! example

    For example if we want to add a new endpoint named `geocode`:
    ```
        git checkout -b "add endpoint geocode in v1"
    ```
    Now we develop at the new endpoint, means we create
    `app/endpoints/v1/geocode.py` and add the input- and output-model for the
    new endpoint inside `app/endpoints/v1/models.py`.
    If we need additional error-codes we define them in
    `app/endpoints/v1/errors.py`.

We add each change with:
```bash
    git add <filename_with_changes>
    git commit -m '<short_description>' -m '<long_description>'
```

!!! example

    In the example creating the new endpoint geocode this could be:
    ```
        git add app/endpoints/v1/geocode.py
    ```
    
    and then
    ```
        git commit -m 'added new endpoint /api/v1/geocode' -m 'this endpoint ...'
    ```

If we are done with this task and have implemented everything needed for this
new feature we run the following commands:
```bash
    git checkout devl
    git pull
    git checkout <feature_branch_name>
    git rebase devl
    git push
```

!!! example

    In the example this would be:
    ```
        git checkout devl
    ```
    
    followed by
    ```
        git pull
    ```
    to ensure the local `devl-branch` is up to date.
    
    Then we change back to the `feature-branch`:
    ```
        git checkout "add endpoint geocode in v1"
    ```
    
    We rebase the `feature-branch` on the updated `devl-branch`:
    ```
        git rebase devl
    ```
    
    Finally we can push our local `feature-branch` to the remote:
    ```
        git push
    ```

!!! info

    Explanaition:
    We ensure the local `devl-branch` to be up to date.
    Then we `rebase` the local `feature-branch` on the updated local
    `devl-branch`.
    This ensures a linear commit style.

After a `code review` the reviewer merges this remote `feature-branch` into the
remote `devl-branch` using:
```bash
    git checkout devl
    git pull
    git merge --no-ff <feature_branch_name>
    git push
```

!!! example

    In our example this would be:
    ```
        git checkout devl
    ```
    
    After the reviewer changed to the local `devl-branch` he updates the local
    `devl-branch` with the remote:
    ```
        git pull
    ```
    
    Then he merges the `feature-branch` into the `devl-branch`:
    ```
        git merge --no-ff "add endpoint geocode in v1"
    ```

    Now he can push the updated local `devl-branch` to the remote:
    ```
        git push
    ```

!!! info

    The reviewer ensures his local `devl-branch` and the remote `devl-branch`
    are up to date.
    Then he merges the local `feature-branch` into the local `devl-branch`.
    The updated local `devl-branch` (now including the changes from the local
    `feature-branch`) is then pushed to the remote `devl-branch`.


After testing the `devl-branch` and the review the `devl-branch` can be merged
into the `staging-branch`.
Then additional tests and reviews are done.
If they pass, the `staging-branch` is merged into `master-branch` /
`production-branch`.
