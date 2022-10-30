# Terminal
This file contains information about the terminal. The information in this file is based on the [Platzi terminal course](https://platzi.com/clases/2292-terminal).

## Commands

### Paths

| Path | Description |
| :--- | :--- |
| `~` | The home directory. |
| `.` | The current directory. |
| `..` | The parent directory. |
| `/` | The root directory. |

### Keyboard shortcuts

| Shortcut | Description |
| :--- | :--- |
| <kbd>Ctrl</kbd>+<kbd>A</kbd> | Move to the beginning of the line. |
| <kbd>Ctrl</kbd>+<kbd>E</kbd> | Move to the end of the line. |
| <kbd>Ctrl</kbd>+<kbd>C</kbd> | Cancel the current command. |
| <kbd>Ctrl</kbd>+<kbd>L</kbd> | Clear the terminal screen. |

### Directories

| Command | Description |
| :--- | :--- |
| `pwd` | Print the current working directory. |
| `mkdir <path>` | Create a directory. |
| `cd <path>` | Change the current working directory. |
| ^^ | Without a path, it will change to the home directory. |
| `ls` | List the contents of a directory. |
| ^^ | Flag `-l` to list in long format. |
| ^^ | Flag `-a` to list hidden files. |
| ^^ | Flag `-h` to list in human readable format. |
| ^^ | Flag `-S` to sort by size. |
| ^^ | Flag `-t` to sort by modification time. |
| `tree` | Print the contents of a directory in a tree structure. |
| ^^ | Flag `-L <number>` to specify the depth. |

### Files (and directories)

| Command | Description |
| :--- | :--- |
| `file <path>` | Print information about the type of a file. |
| `touch <file>` | Create a file. |
| `mv <file> <path>` | Move a file or directory. If you specify **two files**, it will rename the first file to the second. |
| `rm <file>` | Remove a file. |
| ^^ | Flag `-i` to ask for confirmation. |
| ^^ | Flag `-r` to remove directories recursively. |
| `cp <file> <path>` | Copy a file or directory. |
| `ln <file> <path>` | Create a hard link. |
| ^^ | Flag `-s` to create a symbolic link. |

### Text files

| Command | Description |
| :--- | :--- |
| `cat <file>` | Print the contents of a file. |
| `head <file>` | Print the first 10 lines of a file. `-n` to specify the number of lines. |
| `tail <file>` | Print the last 10 lines of a file. `-n` to specify the number of lines. |
| `less <file>` | Print the contents of a file. Use <kbd>Space</kbd> or <kbd>Down</kbd> to scroll down, <kbd>Up</kbd> to scroll up, <kbd>Q</kbd> to quit. <kbd>/</kbd> to search. |

### Command help

| Command | Description |
| :--- | :--- |
| `man <command>` | Print the manual of a command. |
| `help <command>` | Print the help of a command. |
| `type <command>` | Print the type of a command. |
| `alias <name>="<command>"` | Create an alias for a command. |
| `which <command>` | Print the location of a command. |
| `whatis <command>` | Print a one-line description of a command. |

### Wildcards

| Wildcard | Description |
| :--- | :--- |
| `*` | Matches any string. |
| `?` | Matches any single character. |
| `[abc]` | Matches any character in the set. |
| ^^ | `[a-z]` matches any character in the range. |
| ^^ | `[!abc]` matches any character not in the set. |
| `[[:class:]]` | Matches any character in the class. |
| ^^ | `[[:alnum:]]` matches any alphanumeric character. |
| ^^ | `[[:alpha:]]` matches any alphabetic character. |
| ^^ | `[[:digit:]]` matches any digit. |
| ^^ | `[[:lower:]]` matches any lowercase character. |
| ^^ | `[[:upper:]]` matches any uppercase character. |

### Pipes

| Command | Description |
| :--- | :--- |
| `<command> < <file>` | Redirect the input of a command to a file. |
| `<command> > <file>` | Redirect the output of a command to a file. |
| `<command> >> <file>` | Append the output of a command to a file. |
| `<command> 2> <file>` |### Wildcards

| Wildcard | Description |
| :--- | :--- |
| `*` | Matches any string. |
| `?` | Matches any single character. |
| `[abc]` | Matches any character in the set. |
| ^^ | `[a-z]` matches any character in the range. |
| ^^ | `[!abc]` matches any character not in the set. Redirect the error output of a command to a file. |
| `<command1> | <command2>` | Pipe the output of a command to another command. |
| `<command1> & <command2>` | Run two commands in parallel. |
| `<command1> ; <command2>` | Execute two commands sequentially. |
| `<command1> || <command2>` | Execute a command if the previous command failed. |
| `<command1> && <command2>` | Execute a command if the previous command succeeded. |

### Permissions

| Octal | Binary | Permission |
| :--- | :--- | :--- |
| `0` | `000` | No permissions. `---` |
| `1` | `001` | Execute permission. `--x` |
| `2` | `010` | Write permission. `-w-` |
| `3` | `011` | Write and execute permissions. `-wx` |
| `4` | `100` | Read permission. `r--` |
| `5` | `101` | Read and execute permissions. `r-x` |
| `6` | `110` | Read and write permissions. `rw-` |
| `7` | `111` | Read, write, and execute permissions. `rwx` |

#### Groups and users

| Symbol | Description |
| :--- | :--- |
| `u` | User. |
| `g` | Group. |
| `o` | Other (world). |
| `a` | All. |

##### Commands

| Command | Description |
| :--- | :--- |
| `id` | Print the users and group ID. |
| `whoami` | Print the current user. |
| `su <user>` | Switch to another user. |
| `sudo <command>` | Execute a command as the superuser. |
| `groups` | Print the groups of the current user. |


#### Change permissions
Example to change the permissions of a file to:

| Command | Description |
| :--- | :--- |
| `chmod u=rwx, go+rx <file>` | Read, write, and execute permissions for the user, and read and execute permissions for the group and other. |


### Environment variables

| Command | Description |
| :--- | :--- |
| `env` | Print the environment variables. |
| `echo $<VAR>` | Print the value of a variable. |
| `export <VAR>=<value>` | Set the value of a variable. |


### Search

| Command | Description |
| :--- | :--- |
| `find <path> -name <pattern>` | Find files by name. |
| `grep <pattern> <file>` | Search for a pattern in a file. |
| ^^ | Flag `-i` to ignore case. |


### Network

| Command | Description |
| :--- | :--- |
| `ifconfig` | Print the network interfaces. |
| `ping <ip_domain>` | Ping a host. |
| `curl <ip_domain>` | Send a request to a host and print the response. |
| `wget <ip_domain>` | Download a file from a host. |
| `traceroute <ip_domain>` | Print the route to a host. |
| `netstat` | Print the network connections. |
| ^^ | Flag `-i` to print the network interfaces. |
| ^^ | Flag `-t` to print the TCP connections. |


### Compression

| Command | Description |
| :--- | :--- |
| `tar -czvf <file.tar.gz> <file/directory>` | Create a tar archive. |
| `tar -xzvf <file.tar.gz>` | Extract a tar archive. |