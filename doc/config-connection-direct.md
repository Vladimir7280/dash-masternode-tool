# Connection to a local FIX daemon
In this scenario, you will use your own FIX daemon configured to serve JSON-RPC requests on your local network or any network you can access directly. The most convenient way to achieve this is to run a daemon on the same computer as the FIXMT application itself.

## Install the FIX Core wallet
We will use the official FIX Core client as the FIX daemon for this configuration. Install it now if not already installed. Binary installers for macOS, Linux and Windows can be downloaded from the [official site](https://www.fix.org/wallets), while documentation on the installation process is available on the [FIX Wiki](https://docs.fix.org/en/stable/wallets/fixcore/installation.html).

## Enable JSON-RPC and "indexing" in FIX Core
###  Set the required parameters in the `fix.conf` file
The default FIX Core configuration does not include all of the required settings, so some changes to the `fix.conf` file are necessary. The location of this file varies depending on the operating system you are using and may be changed during installation, so paths will not be specified here due to possible confusion. Instead, select `Tools -> Open Wallet Configuration File` from the FIX Core menu. The `fix.conf` file will open in your default text editor.

Copy and paste the following parameters/values into the file, changing the `rpcuser` and `rpcpassword` values to your own unique values:
```ini
rpcuser=any_alphanumeric_string_as_a_username
rpcpassword=any_alphanumeric_string_as_a_password
rpcport=9998
rpcallowip=127.0.0.1
server=1
addressindex=1
spentindex=1
timestampindex=1
txindex=1
```

### Restart FIX Core

Close FIX Core by selecting `File -> Exit` from the menu, then open it again.

### Rebuild index
Setting parameters related to indexing and even restarting the application is not enough for FIX Core to entirely update its internal database to support indexing, so it is necessary to force the operation. Follow the following steps to do so:

 * Select the `Tools -> Wallet Repair` menu item.
 * Click the `Rebuild index` button in the Wallet Repair dialog box.  
    ![Wallet repair rebuild index](img/fixqt-rebuild-index.png)
 * Wait until the operation is complete. This step may take several hours.

## Configure connection in the FIXMT
 * Open FIXMT and click the `Configure` button.
 * Select the `FIX network` tab.
 * Click the `+` (plus) button on the left side of the dialog.
 * Check the `Enabled` box.
 * Enter the following values:
   * `RPC host`: 127.0.0.1
   * `port`: 9998
   * `RPC username`: enter the value you specified for the `rpcuser` parameter in the `fix.conf` file.
   * `RPC password`: enter the value you specified for the `rpcpassword` parameter in the `fix.conf` file.
 * Make sure the `Use SSH tunnel` and `SSL` checkboxes remain unchecked. Also, if you decide to use only this connection, deactivate all other connections by unchecking the corresponding `Enabled` checkboxes.  
    ![Direct connection configuration window](img/fixmt-config-dlg-conn-direct.png)
 * Click the `Test connection` button. If successful, FIXMT will return the following message:  
    ![Connection successful](img/fixmt-conn-success.png)
