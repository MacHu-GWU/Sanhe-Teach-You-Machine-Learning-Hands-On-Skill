An example of using machine learning to predict gold price
==============================================================================

- `Source Code <https://github.com/MacHu-GWU/Sanhe-Teach-You-Machine-Learning-Hands-On-Skill/blob/master/gold_price_predict-project/example.py>`_

- `Plot <https://github.com/MacHu-GWU/Sanhe-Teach-You-Machine-Learning-Hands-On-Skill/blob/master/gold_price_predict-project/example.png>`_

.. note::

    This example is not usuable in real world, because in order to predict 3 days
    later's price, u need to know mean price of most recent X days, which is not
    available in real world. THIS IS JUST A DEMO.

For Windows, make sure you installed bash and gnu make (OR BUY YOU SELF A MAC), follow these tutorial:

- https://github.com/MacHu-GWU/Dev-Exp-Share/blob/master/OS/Windows10/Bash-in-Windows.rst
- https://github.com/MacHu-GWU/Dev-Exp-Share/blob/master/OS/Windows10/Makefile-in-Windows.rst

Set up virtual environment and install dependencies::

    $ make up
    $ make dev_install

Run ``example.py``:

    $ make run_example
