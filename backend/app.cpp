#include <iostream>
#include <unistd.h>

using namespace std;

int main() {
    char hostname[256];
    gethostname(hostname, sizeof(hostname));
    cout << "Served by backend: " << hostname << endl;
    return 0;
}
