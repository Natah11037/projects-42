*This project has been created as part of the 42 curriculum by cyakisan and nweber--*

/************************************/
/*          FT_DESCRIPTION          */
/************************************/
{
    project push_swap is a program created to sort a random list of numbers with different system of algorithm;
    the program give the list of operations needed to sort the list correctly;
    the program choose, by the disorder percentage of the random list given, between three optimized algorithm
    {
        if the disorder percentage is less than twenty percent the program is going to choose the insertion sort algorithm;
        if the disorder percentage is between twenty and fifty percent the program is going to choose the chunk sort algorithm;
        if the disorder percentage is more than fifty percent the program is going to choose the radix sort algorithm;
    }
    the insertion sort algorithm is an algorithm that take the list and verified if there is numbers that are already at the good placement. if they are they stay in the first list if not they go in the second list. once the program did that he's gonna put the numbers in the second list again in the first list but in the good order this time;
    the chunk sort algorithm is an algorithm that take the list and take the size_of_the_chunk lower numbers in the first list and put them in the second. then he do that until the first list is empty. now he just sort in the chunk pushing in the first list in the good order;
    the radix sort algorithm is an algorithm that check the first byte of evry number in the first list and push in the second every number that has the first byte to 0. then repushing in the first list and checking the next byte until the last byte is checked;
}

/************************************/
/*          FT_INSTRUCTION          */
/************************************/
{
    to compil and create an executable you need to do the command make;
    to create a random list of numbers sort in a random disorder you can make the command : shuf -i 0-500 -n 500 > [nom du fichier]
    then do the command : ./push_swap [you can put flag here like --simple --medium --complex or --adaptative] $(cat [nom du fichier])
}