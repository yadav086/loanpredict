import streamlit as st
import pickle

model_rf = pickle.load(open('rf_pickle.pkl','rb'))
model_kn = pickle.load(open('kn_pickle.pkl','rb'))
model_dc= pickle.load(open('dc_pickle.pkl','rb'))

def loan_data():
	st.title('Welcome to loan predection web page!!')
	html_temp="""
	 <br></br>
	 <div style="background-color:cyan ; padding :10px">
	 <style>h1{color: red;}</style>
	 </div>
	"""
	st.markdown(html_temp,unsafe_allow_html=True)
	activities =['Random forest','Decision Tree','K nearest neighbor']
	option = st.sidebar.selectbox('which model you want to select?',activities)


	ApplicantIncome = st.slider('Select the applicant income',0,10000000)

	LoanAmount = st.slider('Select the loan amount',0,10000000)

	LoanAmountTerm = st.selectbox('Available loan amount term are ',(12,36,60,84,120,180,240,300,360,480))

	Credit_History = st.radio("Credit score",('Good', 'bad'))

	if Credit_History=='Good':
		Credit_History=1
	else:
		Credit_History=0

	Property_Area=st.selectbox('Available Property Area ',('Urban','Rural','Semi urban'))
	if Property_Area =='Urban':
		Property_Area=1
	elif Property_Area =='Rural':
		Property_Area=2
	else:
		Property_Area=3

	inputs =[[ApplicantIncome,LoanAmount,LoanAmountTerm,Credit_History,Property_Area]]
	print(inputs)

	if option =='Random forest':
		model_rf.predict(inputs)			
	elif option =='Decision Tree':
		model_dc.predict(inputs)
	else:
		model_kn.predict(inputs)
	
	if st.button('Predict'):
		if model_rf.predict(inputs)[0]==0 or model_dc.predict(inputs)[0]==0 or model_kn.predict(inputs)[0]==0:
			st.success('Your Loan is rejected')
		else:
			st.success('Your Loan is accepted')


if __name__=='__main__':
	loan_data()




