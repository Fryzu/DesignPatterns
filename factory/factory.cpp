#include "factory.hpp"

//Warrior

std::string Warrior::name = "Warrior";
std::string Warrior::getName() const {
    
    std::stringstream result;

    result << "I am a " << name << ". I can use my sword!" << std::endl;

    return result.str();

}

//Archer

std::string Archer::name = "Archer";
std::string Archer::getName() const {
    
    std::stringstream result;

    result << "I am a " << name << ". I can use my bow!" << std::endl;

    return result.str();

}

//Factory

Enemy* EnemyFactory::generateEnemy() {

    auto seed = std::time(nullptr);
    std::srand(seed);

    int randomVar = std::rand()%2;

    Enemy* resultEnemy = nullptr;

    if (randomVar == 1) {
        Enemy* resultEnemy = new Warrior();
    }
    else {
        Enemy* resultEnemy = new Archer();
    }

    return resultEnemy;
}