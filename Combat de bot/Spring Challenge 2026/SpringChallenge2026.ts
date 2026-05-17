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

    public getPosition(): Position {
        return {
            x: this.x,
            y: this.y
        }
    }

    public isTrollCanStillCarry(): boolean {
        let isTrollCanCarry: boolean = true;
        let totalTrollActuallyCarry: number = (this.carryPlum + this.carryLemon + this.carryApple + this.carryBanana + this.carryIron + this.carryWood);
        if (this.carryCapacity <= totalTrollActuallyCarry) {
            isTrollCanCarry = false;
        }
        return isTrollCanCarry;
    }
}

class Tree {
    type: string;
    x: number;
    y: number;
    size: number;
    health: number;
    fruits: number;
    cooldown: number;

    constructor(type: string, x: number, y: number, size: number, health: number, fruits: number, cooldown: number) {
        this.type = type;
        this.x = x;
        this.y = y;
        this.size = size;
        this.health = health;
        this.fruits = fruits;
        this.cooldown = cooldown;
    }

    public isTreeHaveFruit() : boolean {
        if (this.fruits > 0) {
            return true;
        } else {
            return false;
        }
    }

    public getPosition(): Position {
        return {
            x: this.x,
            y: this.y
        }
    }
}

class GameMap {
    width: number;
    height: number;
    line: string[][];
    
    constructor(width: number, height: number, line: string[][]) {
        this.width = width;
        this.height = height;
        this.line = line;
    }
    
    public getMyShack(): Position {
        let searching: string = '0';
        let i: number = 0;
        let index: number = -1;
        while (index === -1) {
            index = this.line[i].indexOf(searching);
            i++;
        }
        i--;
        return {
            x: index,
            y: i
        }
    }

    public getMyShackOutline(): Position[] {
        return [
            {
                x: this.getMyShack().x + 1,
                y: this.getMyShack().y
            },
            {
                x: this.getMyShack().x - 1,
                y: this.getMyShack().y
            },
            {
                x: this.getMyShack().x,
                y: this.getMyShack().y + 1
            },
            {
                x: this.getMyShack().x,
                y: this.getMyShack().y - 1
            }
        ]
    }
}

class Pantry {
    plum: number;
    lemon: number;
    apple: number;
    banana: number;
    iron: number;
    wood: number;

    constructor(plum: number, lemon: number, apple: number, banana: number, iron: number, wood: number) {
        this.plum = plum;
        this.lemon = lemon;
        this.apple = apple;
        this.banana = banana;
        this.iron = iron;
        this.wood = wood;
    }
}

type Position = {
    x: number;
    y: number;
}

const lineArray: string[][] = [];
var inputs: string[] = readline().split(' ');
const width: number = parseInt(inputs[0]);
const height: number = parseInt(inputs[1]);
for (let i = 0; i < height; i++) {
    const line: string = readline();
    lineArray.push(line.split(""));;
}

const gameMap = new GameMap(width, height, lineArray);
const shackPosition: Position = gameMap.getMyShack();
const shackOutline: Position[] = gameMap.getMyShackOutline();

console.error(gameMap.getMyShackOutline());

while (true) {
    const trolls: Troll[] = [];
    const trees: Tree[] = [];
    const pantry: Pantry[] = [];

    initial(trolls, trees, pantry)

    const myTrolls: Troll[] = trolls.filter(troll => troll.player === 0);
    let treesWithFruits: Tree[] = trees.filter(tree => tree.isTreeHaveFruit());

    const trollsAction: string[] = [];

    for (const troll of myTrolls) {
        let betterTreePosition: Position = findBetterTreePosition(troll, treesWithFruits);
        treesWithFruits = cleanTreesWithFruits(betterTreePosition, treesWithFruits);

        const nextAction: string = findNextAction(troll, betterTreePosition, shackPosition);
        trollsAction.push(nextAction);
    }

    const action: string = trollsAction.join("; ");
    const train: string = isTrollToTrain(myTrolls, pantry[0]);

    console.log(action + ";" + train);
}

function findNextAction(troll: Troll, betterTreePosition: Position, shackPosition: Position): string {
    let nextAction: string = "";
    const trollPosition: Position = troll.getPosition();
    if (troll.isTrollCanStillCarry()) {
        if ((betterTreePosition.x === trollPosition.x && betterTreePosition.y === trollPosition.y)) {
            // Ne possède pas assez de ressource, est près d'un arbre avec des fruits, doit récolté
            nextAction = "HARVEST"+ " " + troll.id;
        } else {
            // Ne possède pas assez de ressource, n'est pas près d'un arbre avec des fruits, doit rejoindre l'arbre avec des fruits le plus proche
            nextAction = "MOVE" + " " + troll.id + " " + betterTreePosition.x + " " + betterTreePosition.y;
        }
    } else {
        if ((shackPosition.x === (trollPosition.x - 1) && shackPosition.y === trollPosition.y) || (shackPosition.x === (trollPosition.x + 1) && shackPosition.y === trollPosition.y) || (shackPosition.x === trollPosition.x && (shackPosition.y === trollPosition.y - 1)) || (shackPosition.x === trollPosition.x && (shackPosition.y === trollPosition.y + 1))) {
            // possède assez de ressource, est près du shack, doit déposer les fruits
            nextAction = "DROP" + " " + troll.id;
        } else {
            // possède assez de ressource, doit rejoindre le Shack
            nextAction = "MOVE" + " " + troll.id + " " + shackPosition.x + " " + shackPosition.y;
        }
    }
    
    return nextAction;
}

function findBetterTreePosition(troll: Troll, treesWithFruits: Tree[]): Position {
    const trollPosition: Position = troll.getPosition();

    let betterRatio: number = Infinity;
    let betterTreePosition: Position = {
        x: 0,
        y: 0
    }

    for (const treeWithFruits of treesWithFruits) {
        const treePosition: Position = treeWithFruits.getPosition();
        
        const DistanceTrollTree: number = computeDistanceTrollTree(trollPosition, treePosition)
        
        if (DistanceTrollTree < betterRatio) {
            betterRatio = Math.abs((trollPosition.x - treePosition.x)) + Math.abs((trollPosition.y - treePosition.y));
            betterTreePosition = treePosition;
        }
    }

    return betterTreePosition;
}

function cleanTreesWithFruits(betterTreePosition: Position, treesWithFruits: Tree[]): Tree[] {
    return treesWithFruits.filter(treeWithFruits => treeWithFruits.x !== betterTreePosition.x && treeWithFruits.y !== betterTreePosition.y);
}

function computeDistanceTrollTree(trollPosition: Position, treePosition: Position): number {
    return Math.abs((trollPosition.x - treePosition.x)) + Math.abs((trollPosition.y - treePosition.y));
}

function isTrollToTrain(myTrolls: Troll[], pantry: Pantry): string {
    if (myTrolls.length === 1 && pantry.lemon === 10) {
        return " TRAIN" + " " + 1 + " " + 3 + " " + 1 + " " + 0;
    }
    return "";
}

function initial(trolls: Troll[], trees: Tree[], pantry: Pantry[]) {
    for (let i = 0; i < 2; i++) {
        var inputs: string[] = readline().split(' ');
        const plum: number = parseInt(inputs[0]);
        const lemon: number = parseInt(inputs[1]);
        const apple: number = parseInt(inputs[2]);
        const banana: number = parseInt(inputs[3]);
        const iron: number = parseInt(inputs[4]);
        const wood: number = parseInt(inputs[5]);
        pantry.push(new Pantry(plum, lemon, apple, banana, iron, wood));
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
        trees.push(new Tree(type, x, y, size, health, fruits, cooldown));
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
}
