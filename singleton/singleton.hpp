#ifndef LETTERS
#define LETTERS

#include <boost/thread.hpp>
#include <boost/date_time/posix_time/posix_time.hpp>
#include <stdexcept>
#include <iterator>
#include <vector>

class LettersSingleton {

    private:
        static LettersSingleton* singletonInstance;
        static bool firstThread;
        LettersSingleton();

        std::vector<char> letters;
        static char scrabbleLetters[100];

    public:
        static LettersSingleton& getInstance();
        int getLettersSize();

};

#endif