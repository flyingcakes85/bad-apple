This folder contains the code required to play Bad Apple Video on GitHub Contributions Graph.

In the video, I piped outputs into an alias `cpy`. This simply copied the text onto my clipboard. I have the following line in my `~/.zshrc`
```sh
alias cpy="xclip -sel clip"
```

Run `python ascii_gen.py` to generate frames in a folder called `ascii_frames`. Copy this folder to your server root. On [line 26 of file `js_function.js`](https://github.com/flyingcakes85/bad-apple/blob/main/github-contributions/js_function.js#L26), change `127.0.0.1` to your server root. I used a local Apache Httpd server for my video. You will need to disable csp in your browser config and also bypass CORS. Make sure to revert these settings later on, since these can be a security risk.

Compile and run `canvas_gen.cpp` and copy its output. Open a profile page on GitHub. Using inspect element, locate the svg element that cantains the grid. Increase height of this element (I set it to 722). Right click on the first child of this element and select "Edit as HTML". Remove the existing code and paste what you just copied.

Next, Copy the contents of `js_function.js` and paste in the console tab. Finally run `renderApple()` in the console to play the video. To stop playing the video midway, run `br = 4` in the console.

To change frame rate of video, edit [line 42 of `js_function.js`] and change `250` to a different value. This is the time in milliseconds to wait between consecutive frames. 250ms is 4fps and this is the frame rate at which I recorded my video. 

I edited my video using [Kdenlive](https://kdenlive.org/en/).
