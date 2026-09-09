#include<iostream>
#include<vector>
using namespace std;

int main(){
    int arr[]={1, 2, 3, 4, 5,};
    int size = 5;

    int maxsum = INT_MIN;

    for(int st=0; st<size; st++){
        int currsum=0;
        for(int end=st; end<size; end++){
            currsum += arr[end];
            maxsum = max(currsum ,maxsum);
    }
}
    cout<<" maxsum ="<<maxsum<<endl;
    return 0;
}
