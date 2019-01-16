/**
 * Note: The returned array must be malloced, assume caller calls free().
 Running time: 0sec
 */
#define LIST_LENGTH 1000

typedef struct Item Item;

struct Item{
    int value;
    int index;
    Item * next;
};
typedef struct List{
    Item *head;
    Item *end;
}List;
void insertItem(List *list, Item *item){
    int key = (unsigned int) (item->value) % LIST_LENGTH;
    if(!list[key].head){
        list[key].head = item;
        list[key].end = item;
    }else{
        list[key].end->next = item;
        list[key].end = item;
    }
}
int searchValue(List *list, int value){
    int key = (unsigned int)(value) % LIST_LENGTH;
    Item *p = list[key].head;
    while(p){
        if(value == p->value){
            return p->index + 1;
        }
        p = p->next;
    }
    return 0;
}
int* twoSum(int* nums, int numsSize, int target) {
    //allocate memory
    int *res = (int*) malloc (2 * sizeof(int));
    List list[LIST_LENGTH];
    memset(list, 0, sizeof(Item) * LIST_LENGTH);
    Item item[numsSize];
    memset(item, 0, sizeof(Item) * numsSize);
    
    for(int i = 0; i < numsSize; i++){
        item[i].value = nums[i];
        item[i].index = i;
        insertItem(list, &item[i]);
    }
    for(int i = 0; i < numsSize; i++){
        int x = i + 1;
        int y = searchValue(list, target - nums[i]);
        if(x && y && (x ^ y)){
            x--;
            y--;
            res[0] = x < y ? x : y;
            res[1] = x + y - res[0];
            break;
        }
    }
    return res;
}
