import streamlit as st
def depreciation(cost, rate, yearofpur, yearofsale, dep_type, accum = 0):
    if dep_type == 'Reducing Balance Method':
        return round(((1-rate/100)**(yearofsale-yearofpur))*(cost-accum))
    else:
        return (cost-((yearofsale-yearofpur)*((rate/100)*cost)))

print(depreciation(1000000,10,2016,2019,'rbm', 100000))


def depn_sol(cost, rate, yearofpur, yearofsale, dep_type='slm', method = 1, accum = 0):
    yearend = yearofpur
    yearendlist = []
    cost = cost
    showdepn = []
    depreciated = []
    resultnbv = []
    cost = cost - accum
    currentcost = cost
    if method == 1:
        st.subheader('Method 1')
        if dep_type == 'Reducing Balance Method':
            while yearend < yearofsale:
                yearendlist.append(yearend)
                showdepn.append(f'{rate}% of {currentcost}')
                cur = currentcost
                depr = (rate/100) * currentcost
                currentcost = (1-rate/100)*currentcost
                depreciated.append(f'{depr}')
                resultnbv.append(f'{cur}-{depr} = {currentcost}')
                yearend+=1
            if yearofsale - yearofpur != 0:
                st.dataframe({'Year End': yearendlist,'Calculation': showdepn,'Depreciated': depreciated,'NBV': resultnbv}, width = 1500, height = 200)
            st.success(f'The resulting Net Book Value is {currentcost}')
        else:
            while yearend < yearofsale:
                yearendlist.append(yearend)
                showdepn.append(f'{rate}% of {cost}')
                depr = (rate/100) * cost
                depreciated.append(f'{depr}')
                cur = currentcost
                currentcost -= depr
                resultnbv.append(f'{cur}-{depr} = {currentcost}')
                yearend+=1
            if yearofsale - yearofpur != 0:
                st.dataframe({'Year End': yearendlist,'Calculation': showdepn,'Depreciated': depreciated,'NBV': resultnbv}, width = 1500, height = 200)
            st.success(f'The resulting Net Book Value is {currentcost}')

    elif method == 2:
        st.subheader('Method 2')
        if dep_type == 'Reducing Balance Method':
            yearofpur = int(yearofpur)
            yearofsale = int(yearofsale)
            cost = cost
            st.markdown(f'( ( 100% - {rate}% ) ^ ( {yearofsale} - {yearofpur} ) ) \* {cost}')
            returnrate = 100-rate
            years = yearofsale-yearofpur
            st.markdown(f'( {returnrate}% ^ {years} ) \* {cost}')
            st.markdown(f'( {returnrate/100} ^ {years} ) \* {cost}')
            calc = (returnrate/100)**years
            st.markdown(f'{calc} * {cost}')
            st.success(f'The resulting Net Book Value is {calc*cost}')
        else:
            st.markdown(f'{cost} - ( ( {yearofsale} - {yearofpur} ) * ( {cost} \* {rate}% ) )')
            st.markdown(f'{cost} - ( {yearofsale - yearofpur} * ( {cost} \* {rate/100} ) )')
            st.markdown(f'{cost} - ( {yearofsale - yearofpur} * {cost * (rate/100)} )')
            calculate = (yearofsale-yearofpur) * (cost*(rate/100))
            st.markdown(f'{cost} - {calculate}')
            st.success(f'The resulting Net Book Value is {cost-calculate}')


def help_depn_sol(cost, rate, yearofpur, yearofsale, dep_type='slm', method = 1, accum = 0):
    if dep_type == 'Reducing Balance Method':
        if method == 1:
            st.markdown('This is the official CAIE method. The other can be used for error checking (I don\'t know if that method is allowed to be used)')
            st.markdown('As a general rule, you apply depreciation in the year of purchase but not in year of sale')
            st.markdown('For each year, you draw a row. In reducing balance method the rate of depreciation is applied to NBV(Netbook Value), which is cost - accumulated depreciation, instead of the cost')
            st.markdown('For example in the first year, NBV = Purchase Cost, so you apply depreciation on cost')
            st.markdown('In the following years, you apply depreciation to NBV instead of Purchase Cost, unlike straight line method')
            st.markdown(f'In this example, in the first year, {yearofpur}, depreciation is applied to the Purchase Cost')
            st.markdown(f'The Depreciation comes out to be {rate/100*cost} which is then subtracted from the purchase cost to return NBV')
            st.markdown(f'In the following year, depreciation is then applied to the following years')
            st.markdown(f'Depreciation is not applied in {yearofsale}, which is the year of sale')
            st.markdown(f'The NBV calculated after depreciating at year end, {yearofsale-1}, is the answer, which in this case is **{round(((1-rate/100)**(yearofsale-yearofpur))*(cost-accum))}**')
        elif method == 2:
            st.markdown('''This solution follows the general formula of **NBV = Purchase Cost - Depreciation**, where Depreciation is calculated by:''')
            st.markdown('Depreciation = rateʸᵉᵃʳ ᵒᶠ ˢᵃˡᵉ ⁻ ʸᵉᵃʳ ᵒᶠ ᴾᵘʳᶜʰᵃˢᵉ * (cost - accumulated cost)')
            st.write('')
            st.markdown(f'Which in this case is Depreciation = {rate}%^({yearofsale}-{yearofpur}) * ({cost}-{accum})')
            st.markdown(f'This adds upto {cost - (round(((1-rate/100)**(yearofsale-yearofpur))*(cost-accum)))}')
            st.markdown(f'NBV = {cost} - {cost - (round(((1-rate/100)**(yearofsale-yearofpur))*(cost-accum)))}')
            st.markdown(f'NBV = {cost - (cost - (round(((1-rate/100)**(yearofsale-yearofpur))*(cost-accum))))}')
    else:
        if method == 1:
            st.markdown('This is the official CAIE method. The other can be used for error checking (I don\'t know if that method is allowed to be used)')
            st.markdown('As a general rule, you apply depreciation in the year of purchase but not in year of sale')
            st.markdown('For each year, you draw a row. In reducing balance method the rate of depreciation is applied to Purchase Cost each year, instead of the NBV(Netbook Value)')
            st.markdown(f'Each year you calculate depreciation by multiplying the rate with cost, which in this case if {rate}% * {cost}')
            st.markdown(f'You subtract the result of rate*cost, which is {rate/100*cost} here, from the Purchase Cost to find the NBV in the first year')
            st.markdown(f'In the following years, new NBV = current NBV - depreciation')
            st.markdown(f'Depreciation is not applied in {yearofsale}, which is the year of sale')
            st.markdown(f'The NBV calculated after depreciating at year end, {yearofsale-1}, is the answer, which in this case is **{(cost-((yearofsale-yearofpur)*((rate/100)*cost)))}**')



        elif method == 2:
            st.markdown('''This solution follows the general formula of **NBV = Purchase Cost - Depreciation**, where Depreciation is calculated by:''')
            st.markdown('Depreciation = (Year of Sale - Year of Purchase) \* rate * cost')
            st.markdown(f'Which in this case is Depreciation = ({yearofsale}-{yearofpur}) \* {rate}% * {cost}')
            st.markdown(f'This adds upto {(yearofsale-yearofpur) * rate/100 * cost}')
            st.markdown(f'NBV = {cost} - {(yearofsale-yearofpur) * rate/100 * cost}')
            st.markdown(f'NBV = {cost - ((yearofsale-yearofpur) * rate/100 * cost)}')



#hef = st.dataframe({'Year End': [2016,2017,2018,2019],'Depreciation': [1,2,3,4],'NBV': ['a','b','c','d']}, width = 250, height = 200)
