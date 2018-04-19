#include <gtest/gtest.h>
#include "factory.hpp"

int main(int argc, char* argv[]) {

    testing::InitGoogleTest(&argc, argv);

    return RUN_ALL_TESTS();

}

TEST(Enemy, Creating) {

    Warrior testWarrior;
    Archer testArcher;

    EXPECT_EQ(testWarrior.getName(), "I am a Warrior. I can use my sword!\n");
    EXPECT_EQ(testArcher.getName(), "I am a Archer. I can use my bow!\n");

}

TEST(EnemyFactory, GenerateEnemy) {

    EnemyFactory testFactory;

    testFactory.generateEnemy();

}