const voreBall = {

    mass: 5,
    speed: 100,
    arrOfMass: [],

    getMass(obj){
        
        this.mass += obj;

        this.speed -= this.mass / 2;
        
    },

    splitMass(times){
        this.arrOfMass = [];
        for(let i = 0; i < times; i++){

            this.arrOfMass.push(this.mass / times)
            
        }
        this.speed = 100;
        this.speed *= times;
    },

    combineMass(){
        
        this.speed /= this.arrOfMass.length;
        this.arrOfMass = [];
    }
    
    }}