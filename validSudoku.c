bool isValidSudoku(char** board, int boardSize, int* boardColSize){
    
    int tmp = 0;
//rows
    for(int i=0;i<9;++i){
        int arr[9] = {0};
        for(int j=0;j<9;++j){
            tmp = board[i][j] - '0';

            if(-2 == tmp)
                continue;

            if(1 == arr[tmp-1]){
                return false;
            }
            arr[tmp-1] = 1;
        }
    }

//columns
    for(int i=0;i<9;++i){
        int arr[9] = {0};
        for(int j=0;j<9;++j){
            tmp = board[j][i] - '0';

            if(-2 == tmp)
                continue;

            if(1 == arr[tmp-1]){
                return false;
            }
            arr[tmp-1] = 1;
        }
    }

//box

    int start_i = 0;
    int start_j = 0;

    for(int box = 1;box<10;++box){
        int arr[9] = {0};
       for(int i=start_i;i<start_i+3;++i) {
           
           for(int j=start_j;j<start_j+3;++j){
               tmp = board[j][i] - '0';

                if(-2 == tmp)
                    continue;

                if(1 == arr[tmp-1]){
                    return false;
                }

                arr[tmp-1] = 1;
           }
       }
        if(0==box%3){
            start_i = 0;
            start_j += 3;
            continue;
        }
        start_i +=3;

    }

    return true;

}