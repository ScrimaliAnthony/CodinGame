// game loop
while (true) {
    var inputs = readline().split(' ');
    const x = parseInt(inputs[0]);
    const y = parseInt(inputs[1]);
    const nextCheckpointX = parseInt(inputs[2]);
    const nextCheckpointY = parseInt(inputs[3]);
    const nextCheckpointDist = parseInt(inputs[4]);
    const nextCheckpointAngle = parseInt(inputs[5]);
    var inputs = readline().split(' ');
    const opponentX = parseInt(inputs[0]);
    const opponentY = parseInt(inputs[1]);

        if (nextCheckpointDist > 4000 &&
           nextCheckpointAngle > -10 && nextCheckpointAngle < 10) {
           console.log(nextCheckpointX + ' ' + nextCheckpointY + ' BOOST');
           }
        else if (nextCheckpointDist < 1500) {
                console.log(nextCheckpointX + ' ' + nextCheckpointY + ' 40');
        }
        else if (nextCheckpointAngle > 50 || nextCheckpointAngle < -50) {
                console.log(nextCheckpointX + ' ' + nextCheckpointY + ' 80');
        }
        else {console.log(nextCheckpointX + ' ' + nextCheckpointY + ' 100');}
}