const character = {

    characterAttributes: {HP: 500,
                          Strength: 120,
                          Speed: 75,
                          Intelligence: 200,
                          Charm: 140,
                          Endurance: 200,
                          Luck: 45
                          },

    weapons: {sword: {damage: 120,
                      speed: 75,
                      damagePerSec: 30},

              arrow: {damage: 100,
                      speed: 45,
                      damagePerSec: 25},

              axe: {damage: 200,
                    speed: 20,
                    damagePerSec: 40},

              shield: {HP: 300,
                       Strength: 250}
              },

    healthBoost(hp) {

        this.characterAttributes.HP += hp;
    },

    // attributeBoost(attr, boost){

    //     this.characterAttributes.attr += boost;
    // },

    enemyAttack(damage) {

        this.characterAttributes.HP -= damage

    },

    mapLocations: ['Egypt', 'Jordan', 'Nigeria', 'South Africa', 'Chad', 'Rwanda', 'Sudan',
                   'Togo', 'Uganda', 'Zimbabwe', 'Libya', 'Kenya', 'Mali', 'Morocco', 'Cameroon']
}