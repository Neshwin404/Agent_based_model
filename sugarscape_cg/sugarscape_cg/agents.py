import math

import mesa


def get_distance(pos_1, pos_2):
    """Get the distance between two point

    Args:
        pos_1, pos_2: Coordinate tuples for both points.

    """
    x1, y1 = pos_1
    x2, y2 = pos_2
    dx = x1 - x2
    dy = y1 - y2
    return math.sqrt(dx**2 + dy**2)


class SsAgent(mesa.Agent):
    def __init__(
        self, unique_id, pos, model, moore=False, sugar=0, metabolism=0, vision=0,age=0,max_age=100,tax=0.05
    ):
        super().__init__(unique_id, model)
        self.pos = pos
        self.age = age
        self.tax=tax
        self.max_age = max_age
        # set max-age random-in-range 60 100
        self.moore = moore
        self.sugar = sugar
        self.metabolism = metabolism
        self.vision = vision
        self.category='ant'
        self.time=0
        self.ad_new=0
        self.benefits=0
        self.earn=0
        

    def get_sugar(self, pos):
        this_cell = self.model.grid.get_cell_list_contents([pos])
        for agent in this_cell:
            if type(agent) is Sugar:
                return agent

    
    def Check_Income_tax(self,val):
        import numpy as np
        # this_cell = self.model.grid.get_cell_list_contents([pos])
        # for agent in this_cell:
        #     if type(agent) is Sugar:
        #         return agent
        # income=list(np.unique(self.model.sdist))
        income=[0,1,2,3,4]
        index = income.index(val)
        # tax_slab=[0,0,5,10,15]
        tax_slab=[]
        for i in range(self.model.main_data['tax_slabs'].loc[self.model.scenario_name]):
            # print(i+1)
            # print(self.model.main_data['tax_slab_'+str(i+1)].loc['first'])
            tax_slab.append(self.model.main_data['tax_slab_'+str(i+1)].loc[self.model.scenario_name])
        # print(val,tax_slab[index])
        indn=index
        
        if sum(income)!=sum(list(np.unique(self.model.sugar_distribution))):   
            import sys
            sys.exit()
        
        income_tax_collected=0
        for i in range(index):
            # print(tax_slab[indn])
            # print(income[indn])
            taxable=income[indn]-income[indn-1]
            income_tax_collected=tax_slab[indn]/100*taxable+income_tax_collected
            # print('tax',tax_slab[indn]/100*taxable,income_tax_collected)
            indn=indn-1
        return income_tax_collected
        
        
        



    def is_occupied(self, pos):
        this_cell = self.model.grid.get_cell_list_contents([pos])
        return any(isinstance(agent, SsAgent) for agent in this_cell)

    def move(self):
        # Get neighborhood within vision
        neighbors = [
            i
            for i in self.model.grid.get_neighborhood(
                self.pos, self.moore, False, radius=self.vision
            )
            if not self.is_occupied(i)
        ]
        neighbors.append(self.pos)
        # Look for location with the most sugar
        max_sugar = max(self.get_sugar(pos).amount for pos in neighbors)
        candidates = [
            pos for pos in neighbors if self.get_sugar(pos).amount == max_sugar
        ]
        # Narrow down to the nearest ones
        min_dist = min(get_distance(self.pos, pos) for pos in candidates)
        final_candidates = [
            pos for pos in candidates if get_distance(self.pos, pos) == min_dist
        ]
        self.random.shuffle(final_candidates)
        self.model.grid.move_agent(self, final_candidates[0])

    def eat(self):
        # total_income_tax=0
        sugar_patch = self.get_sugar(self.pos)
        # print(sugar_patch)
        income_tax=self.Check_Income_tax(sugar_patch.amount)
        # income_tax=self.Check_Income_tax(sugar_patch.amount)
        # print("aburo",self.model.redi)
        if self.time>0:
            self.benefits=(self.model.redi.loc[self.unique_id].benefits)
            # print('JJJJJJJJJ',self.unique_id,self.model.redi)
            self.sugar = self.sugar + sugar_patch.amount- self.metabolism-income_tax+self.benefits
        else:
            # self.benefits=int(self.model.redi.loc[self.unique_id].benefits)
            self.sugar = self.sugar + sugar_patch.amount- self.metabolism-income_tax-0
        # print(sugar_patch.amount,income_tax)
        self.earn=sugar_patch.amount
        self.model.itax=self.model.itax+income_tax
        if self.model.main_data['vision_adaptation'].loc[self.model.scenario_name]=='yes':
            if self.time>0:
                
                # print(self.ad_new.index)
                # print(self.ad_new.loc[self.unique_id].vision_)
                self.vision=int(self.ad_new.loc[self.unique_id].vision_)
            # # self.ad_new.to_csv("ffffffffffffff.csv")
        sugar_patch.amount = 0
        # return total_income_tax
        
        # self.Check_Income_tax(sugar_patch.amount)
    def redist(self):
        # temp_data = self.model.datacollector.get_agent_vars_dataframe()
        # # temp_data=self.datacollector.get_agent_vars_dataframe()
        # # print(temp_data.columns)
        # temp_data=temp_data.loc[temp_data.index[temp_data.category=='ant']]
        # temp_data['Wealth_wa']=temp_data['Wealth']/temp_data['Wealth'].sum()
        # self.model.redi=temp_data
        # print(temp_data['Wealth_wa'].sum())
        # print("collection",self.model.itax_prev/self.model.schedule.get_type_count(SsAgent))
        self.sugar = self.sugar 
        # self.model.itax=self.model.itax+income_tax

        # return total_income_tax
        
        # self.Check_Income_tax(sugar_patch.amount)

    def update_vision(self):
        sugar_patch = self.get_sugar(self.pos)
        self.sugar = self.sugar + sugar_patch.amount- self.metabolism-self.tax*self.sugar
        self.earn=sugar_patch
        
        # for agnt in self.ad_new.index:
        #     print(self.ad_new.loc[agnt].Wealth)
        # print(self.unique_id)
        sugar_patch.amount = 0


    def step(self):
        # self.time=self.time+1
        # print("ss",self.time)
        
        temp_data1=self.model.datacollector.get_agent_vars_dataframe()
        
        temp_data1=temp_data1.loc[temp_data1.index[temp_data1.category=='ant']]
        temp_data1=temp_data1.reset_index(level=[1])
        # (print(temp_data1.loc[temp_data1.index==self.time]))
        temp_data1=temp_data1.loc[temp_data1.index==self.time]
        temp_data1.sort_values(by=['Wealth'])
        
        temp_data1['Wealth_rank'] = temp_data1['Wealth'].rank(method='max')
        temp_data1['Wealth_rank']=temp_data1.Wealth_rank*100/temp_data1.Wealth_rank.max()
        temp_data1['step_']=temp_data1.index      
        temp_data1.index=temp_data1.AgentID
        for ids in temp_data1.index:
            # print(ids)
            wlth=temp_data1.loc[ids].Wealth_rank
            if wlth>=90:
                temp_data1.at[ids,'vision_']=6
            elif wlth <90 and wlth>=80:
                temp_data1.at[ids,'vision_']=5
            elif wlth <80 and wlth>=70:
                temp_data1.at[ids,'vision_']=4                
            elif wlth <70 and wlth>=60:
                temp_data1.at[ids,'vision_']=3   
            elif wlth <60 and wlth>=50:
                temp_data1.at[ids,'vision_']=2                   
            elif wlth <50:
                temp_data1.at[ids,'vision_']=1               

            # elif wlth <50:
            #     temp_data1.at[ids,'vision_']=temp_data1.at[ids,'vision_']+.01
        # print(temp_data1)
        self.ad_new=temp_data1
        # A=(temp_data1['Wealth_rank']<100 & temp_data1['Wealth_rank']>80)
        # for agnt in temp_data1.index:
        #     print(self.ad_new.loc[agnt].Wealth)
        # temp_data1['new_vision']=0
        # temp_data1.nlargest(10, 'Wealth')['new_vision']=4
        # print("ssss",temp_data1['Wealth_rank'].max())
        # temp_data1.to_csv("temp_data111.csv")
        
        
        # apro=pd.read_csv("temp_data111.csv",index_col=0)
        
        self.move()

        self.eat()
        self.redist()

        # print("it_collected",it_collected,total_income_tax)
        self.time=self.time+1
        self.age=self.age+1
        if self.sugar <= 0 or self.age>=self.max_age:
            self.model.grid.remove_agent(self)
            self.model.schedule.remove(self)

            
class Sugar(mesa.Agent):
    def __init__(self, unique_id, pos, model, max_sugar):
        super().__init__(unique_id, model)
        self.amount = max_sugar
        self.max_sugar = max_sugar
        self.sugar=-1
        self.category='sugar'
        self.vision = "sssss"
        self.benefits=0
        self.earn=0
        

    def step(self):
        self.amount = min([self.max_sugar, self.amount + 1])
