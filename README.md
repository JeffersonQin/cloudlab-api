# About

This profile shows how one can instantiate and interact with a Powder Experiment
programmatically in order to accomplish fairly complicated tasks. This approach
will be useful to experimenters with projects that require some level of
automation.

In `powder/experiment.py`, there is a class `PowderExperiment`, which serves as
the main abstraction for starting, interacting with, and terminating a single
Powder experiment. It relies on `powder/rpc.py` for interacting with the Powder
RPC server, and `powder/ssh.py` for interacting with the nodes in the experiment
after they've been stood up.

The example use-case in `main.py` shows how one might use Powder resources in,
e.g., a CI/CD pipeline. It does the following:

1. instantiates a Powder Experiment based on an existing Powder Profile which
   includes two Intel NUC5300s with USRP B210 SDRs;
2. installs some dependencies on the experimental nodes;
3. tunes the CPU settings on the nodes for best performance;
4. clones the OAI RAN source and builds eNB and UE binaries in parallel;
5. starts the eNB and UE in noS1 mode (using tunnel interface, no core network);
6. tests the UE -> eNB uplink with ping.

Logs are collected for each step and parsed in order to verify success/failure.

## Getting Started

### Dependencies

You'll need to use Python3 to run this example. Also, there are a couple of
3rd-party dependencies listed in `requirements.txt` that you'll need to install.

### Credentials

In order to run `main.py` or use an instance of `PowderExperiment` to interact
with the Powder platform, you'll need to have added an ssh key to your Powder
account. If you haven't already done this, you can find instructions
[here](https://docs.powderwireless.net/users.html#%28part._ssh-access%29).
You'll also need to download your Powder credentials. You'll find a button to do
so in the drop-down menu accessed by clicking on your username after logging
into the Powder portal. You'll end up with the file `cloudlab.pem`. Remember
where you put it, because you'll need its path later.

### Running the Example

The RPC client that `PowderExperiment` relies on to interact with the Powder RPC
server requires some variables to be set in the environment. If your private ssh
key is encrypted, it needs to be set in an environment variable as well.

If your ssh key is encrypted:

``` sh
USER=your_powder_username PWORD=your_powder_password \
CERT=/path/to/your/cloulab.pem KEYPWORD=your_ssh_key_password ./main.py
```

If not:

``` sh
USER=your_powder_username PWORD=your_powder_password \
CERT=/path/to/your/cloulab.pem ./main.py
```

It can take more than 30 minutes for all of the steps in `main.py` to complete,
but you'll see intermittent messages on stdout indicating progress. After
completion, the script will print some results and point to the logs generated
during the process.

In some cases, the resources required by the profile used in the example might
not be available. If so, you'll see a log message that indicates as much and the
script will exit. Take a look at the Resource Availability page on the Powder
Portal to see the status of the required nuc5300 nodes.
