
Downloaded Linux Mint xfce version (light version).

**REQUIREMENT**  => The /home folder is located on a separate partition, same disk. For this I'll use this reference:
https://linuxmint-installation-guide.readthedocs.io/en/latest/partitioning.html


1. During the Linux Mint XFCE installation, choose the "Something else" option for partitioning when prompted.
2. You will see a list of available disks. Select the disk you created in VirtualBox (e.g., /dev/sda) and click "New Partition Table" to create a new partition table.
3. Once the new partition table is created, click on the "Free Space" entry and click the "+" button to create a new partition.
4. Configure the partition as follows:
    - Size: Enter the desired size for the /home partition (e.g., 10GB).
    - Type for the new partition: Select "Logical".
    - Location for the new partition: Select "Beginning of this space".
    - Use as: Select "Ext4 journaling file system".
    - Mount point: Select "/home".
5. Click "OK" to create the partition.


![[Pasted image 20230615152346.png]]

1. Select the remaining free space and click the "+" button to create a new partition.
2. Configure the partition as follows:
    - Size: Leave the remaining space as it is to be used for the root partition.
    - Type for the new partition: Select "Logical".
    - Location for the new partition: Select "Beginning of this space".
    - Use as: Select "Ext4 journaling file system".
    - Mount point: Select "/".
3. Click "OK" to create the partition.

![[Pasted image 20230615152611.png]]

![[Pasted image 20230615152638.png]]

Verify the Separate /home Partition

1. Open a terminal (Ctrl+Alt+T).
2. Run the command `lsblk` to list the available block devices.
3. Verify that you see two separate partitions, one mounted as "/" and the other mounted as "/home".

![[Pasted image 20230615160311.png]]

Install LibreOffice, Gimp, 