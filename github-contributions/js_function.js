//function removeAllChildNodes(parent) {
//    while (parent.firstChild) {
//        parent.removeChild(parent.firstChild);
//    }
//}

let i = 0
let d = 0
let br = 0
let frameNumber = 0

function renderApple() {

    if (br == 4) {
        return 0
    }

    if (frameNumber > 599) {
        return 0
    }

    for (i = 0; i < 37; i++) {
        for (d = 0; d < 50; d++) {
            outerBox.children[d].children[i].setAttribute("data-level", frames[parseInt(frameNumber)][i][d])
        }
    }
    frameNumber++
    setTimeout((frameNumber) => {
        renderApple()
    }, 0.033)

}
