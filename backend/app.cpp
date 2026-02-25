#include <iostream>
#include <unistd.h>
#include <limits.h>

using namespace std;

int main() {
    char hostname[HOST_NAME_MAX];
    gethostname(hostname, HOST_NAME_MAX);

    cout << "Served by backend: " << hostname << endl;

    return 0;
}
