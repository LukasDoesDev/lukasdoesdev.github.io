So everyone knows Arch Linux is the superior GNU/Linux distribution (i use arch btw)

Here are the steps I used to use my printer on Arch Linux:

1. Install `cups`, `system-config-printer` and `libcups`

```sh
sudo pacman -S cups system-config-printer libcups
```

2. Enable and start CUPS

```sh
sudo systemctl enable cups
sudo systemctl start cups
```

3. Run `system-config-printer`

```sh
system-config-printer
```

4. Press `Add` in the window that pops up

5. Select your printer

6. Follow the application's instructions

7. You're done! I could just select my printer from Firefox's print menu
