var inputs = readline().split(' ');
const lightX = parseInt(inputs[0]); // the X position of the light of power
const lightY = parseInt(inputs[1]); // the Y position of the light of power
const initialTx = parseInt(inputs[2]); // Thor's starting X position
const initialTy = parseInt(inputs[3]); // Thor's starting Y position

ThorX = initialTx;
ThorY = initialTy;

// game loop
while (true) {
    const remainingTurns = parseInt(readline()); // The remaining amount of turns Thor can move. Do not remove this line.
    
    movementY = "";
    movementX = "";

    if(ThorX > lightX){
        movementX = "W";
        ThorX--;
    } else if(ThorX < lightX) {
        movementX = "E";
        ThorX++;
    }
    
    if(ThorY > lightY) {
        movementY = "N"
        ThorY--;
    } else if(ThorY < lightY) {
        movementY = "S"
        ThorY++;
    }

    console.log(movementY + movementX);
}