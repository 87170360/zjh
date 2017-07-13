#include "XtTypeDeck.h"

int main()
{

	int time_i=0;
	int time_j=0;

	XtTypeDeck deck;

	while(true)
	{


		printf("\n\nBegin FaPai\n");

		for(int i=1; i<=6;i++)
		{
		//	int c_type=i;

			srand(time_i);
			deck.fill();
			XtHoleCards left_card;

			std::map<int,int> card_used;

			int j=0;
			while(true)
			{
				int ret=deck.getHoleCards(&left_card,i);
				if(ret==-1)
				{

					printf("\tcard_used is: ");
					std::map<int,int>::iterator iter;
					for(iter=card_used.begin();iter!=card_used.end();++iter)
					{
						int card_value=iter->first;
						XtCard c(card_value);
						printf("%s ",c.getCardDescription().c_str());
					}

					printf("\n");


					printf("\tMax Type Of Card [%d] is [%d] Srand(%d)\n",i,j,time_i);
					break;
				}
				j++;

				for(unsigned int j=0;j<left_card.m_cards.size();j++)
				{
					int card_value=left_card.m_cards[j].m_value;
					if(card_used.find(card_value) != card_used.end())
					{
						printf("\tCard Error Duble Card,(f %d,s %d) \n",left_card.m_cards[j].m_face,left_card.m_cards[j].m_suit);
						exit(0);
					}
					else 
					{
						card_used[card_value]=1;
					}
				}
			}


		}
		printf("End FaPai\n");
		if(time_i%100000==0)
		{
			time_j++;
			printf("Testing(%d)...\n\n\n",time_j);
		}
		time_i++;
	}

	return 0;
}

