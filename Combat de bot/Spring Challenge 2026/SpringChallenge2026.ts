class Troll {
    id: number;
    player: number;
    x: number;
    y: number;
    movementSpeed: number;
    carryCapacity: number;
    harvestPower: number;
    chopPower: number;
    carryPlum: number;
    carryLemon: number;
    carryApple: number;
    carryBanana: number;
    carryIron: number;
    carryWood: number;

    constructor(id: number, player: number, x: number, y: number, movementSpeed: number, carryCapacity: number, harvestPower: number, chopPower: number, carryPlum: number, carryLemon: number, carryApple: number, carryBanana: number, carryIron: number, carryWood: number) {
        this.id = id;
        this.player = player;
        this.x = x;
        this.y = y;
        this.movementSpeed = movementSpeed;
        this.carryCapacity = carryCapacity;
        this.harvestPower = harvestPower;
        this.chopPower = chopPower;
        this.carryPlum = carryPlum;
        this.carryLemon = carryLemon;
        this.carryApple = carryApple;
        this.carryBanana = carryBanana;
        this.carryIron = carryIron;
        this.carryWood = carryWood;
    }
}

var inputs: string[] = readline().split(' ');
const width: number = parseInt(inputs[0]);
const height: number = parseInt(inputs[1]);
for (let i = 0; i < height; i++) {
    const line: string = readline();
}

while (true) {
    const trolls: Troll[] = [];
    for (let i = 0; i < 2; i++) {
        var inputs: string[] = readline().split(' ');
        const plum: number = parseInt(inputs[0]);
        const lemon: number = parseInt(inputs[1]);
        const apple: number = parseInt(inputs[2]);
        const banana: number = parseInt(inputs[3]);
        const iron: number = parseInt(inputs[4]);
        const wood: number = parseInt(inputs[5]);
    }
    const treesCount: number = parseInt(readline());
    for (let i = 0; i < treesCount; i++) {
        var inputs: string[] = readline().split(' ');
        const type: string = inputs[0];
        const x: number = parseInt(inputs[1]);
        const y: number = parseInt(inputs[2]);
        const size: number = parseInt(inputs[3]);
        const health: number = parseInt(inputs[4]);
        const fruits: number = parseInt(inputs[5]);
        const cooldown: number = parseInt(inputs[6]);
    }
    const trollsCount: number = parseInt(readline());
    for (let i = 0; i < trollsCount; i++) {
        var inputs: string[] = readline().split(' ');
        const id: number = parseInt(inputs[0]);
        const player: number = parseInt(inputs[1]);
        const x: number = parseInt(inputs[2]);
        const y: number = parseInt(inputs[3]);
        const movementSpeed: number = parseInt(inputs[4]);
        const carryCapacity: number = parseInt(inputs[5]);
        const harvestPower: number = parseInt(inputs[6]);
        const chopPower: number = parseInt(inputs[7]);
        const carryPlum: number = parseInt(inputs[8]);
        const carryLemon: number = parseInt(inputs[9]);
        const carryApple: number = parseInt(inputs[10]);
        const carryBanana: number = parseInt(inputs[11]);
        const carryIron: number = parseInt(inputs[12]);
        const carryWood: number = parseInt(inputs[13]);
        trolls.push(new Troll(id, player, x, y, movementSpeed, carryCapacity, harvestPower, chopPower, carryPlum, carryLemon, carryApple, carryBanana, carryIron, carryWood));
    }

    console.error('trolls', trolls);

    console.log('MOVE 0 7 7');
}

    // valid actions:
    // MOVE <id> <x> <y>
    // HARVEST <id> - when you are on the same cell as a tree
    // DROP <id> - when you are next to your shack and carry items