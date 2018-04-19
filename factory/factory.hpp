#ifndef FACTORY
#define FACTORY 

#include <string>
#include <sstream>
#include <cstdlib>
#include <ctime>
#include <iostream>

class Enemy {

    public:
        virtual std::string getName() const = 0;

};

class Warrior : public Enemy {

    private:
        static std::string name;

    public:
        virtual std::string getName() const override;

};

class Archer : public Enemy {

    private:
        static std::string name;

    public:
        virtual std::string getName() const override;

};

class EnemyFactory {

    public:
        Enemy* generateEnemy(); 

};

#endif