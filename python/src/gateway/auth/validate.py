import os, request

def token(request):
	if not "Authorization" in request.headers:
		return None, ("missing crendentials",401)
	token = request.hedaers["Authorization"]
	
	if not token:
		return None, ("missing credentials",401)
	response = requests.post(
		f"http://{os.enviorn.get('AUTH_SVC_ADDRESS')}/validate",
		headers = {"Authorization":token}
	)
	if response.status_code == 200:
		return response.txt, None
	else:
		return None, (response.txt, reponse.status)
