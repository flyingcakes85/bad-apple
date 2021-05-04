
let i = 0
let d = 0
let br = 0
let frameNumber = 1

function renderApple() {

    if (br == 4) {
        br = 0
        return 0
    }

    if (frameNumber > 6572) {
	console.log("conpleted")
        frameNumber = 1
        return 0
    } else if (frameNumber == 1){
    	console.log("started")
    }

   // console.log(frameNumber)

    let frames = []

    fetch('http://127.0.0.1/ascii_frames/' + frameNumber.toString().padStart(4, "0") + '.txt')
        .then(res => res.blob())
        .then(blob => {
            blob.text().then(data => {

                frames = data.split(",")
                frameNumber++
                
                for (i = 0; i < 37; i++) {
                    for (d = 0; d < 50; d++) {
                        let magicNumber = (i * 50) + d
                        outerBox.children[d].children[i].setAttribute("data-level", frames[magicNumber])
                    }
                }
                setTimeout(() => {
                    renderApple()
                }, 250)

            })

        });

}
