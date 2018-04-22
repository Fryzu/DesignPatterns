#include <gtest/gtest.h>
#include <singleton.hpp>

int main(int argc, char* argv[]) {

    testing::InitGoogleTest(&argc, argv);

    return RUN_ALL_TESTS();

}

TEST(LettersSingleton, Constructing) {

    LettersSingleton testObject = LettersSingleton::getInstance();

    EXPECT_EQ(1, 100);

}