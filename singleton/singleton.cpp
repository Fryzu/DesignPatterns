#include <singleton.hpp>

LettersSingleton* LettersSingleton::singletonInstance = nullptr;
bool LettersSingleton::firstThread = true;
char LettersSingleton::scrabbleLetters[100] = {'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a',
	                 'b', 'b', 'c', 'c', 'd', 'd', 'd', 'd', 'e', 'e', 'e', 'e', 'e',
	                 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'f', 'f', 'g', 'g', 'g', 'h',
	                 'h', 'i', 'i', 'i', 'i', 'i', 'i', 'i', 'i', 'i', 'j', 'k', 'l',
	                 'l', 'l', 'l', 'm', 'm', 'n', 'n', 'n', 'n', 'n', 'n', 'o', 'o',
	                 'o', 'o', 'o', 'o', 'o', 'o', 'p', 'p', 'q', 'r', 'r', 'r', 'r',
	                 'r', 'r', 's', 's', 's', 's', 't', 't', 't', 't', 't', 't', 'u',
	                 'u', 'u', 'u', 'v', 'v', 'w', 'w', 'x', 'y', 'y', 'z'};

LettersSingleton& LettersSingleton::getInstance() {

    bool inst = LettersSingleton::singletonInstance == nullptr;
    bool thrd = LettersSingleton::firstThread == true;

    if (inst && thrd) {

        firstThread = false;
        //boost::this_thread::sleep(boost::posix_time::seconds(2));

        try {

            LettersSingleton::singletonInstance = new LettersSingleton();

        }
        catch (const std::bad_alloc& exempt) {

            firstThread = false;

        }

    }

    else {

        return *(LettersSingleton::singletonInstance);

    }

}

LettersSingleton::LettersSingleton() {

    letters = std::vector<char>(scrabbleLetters, scrabbleLetters + sizeof scrabbleLetters / sizeof scrabbleLetters[0]);

}

int LettersSingleton::getLettersSize() {

    return letters.size();

}