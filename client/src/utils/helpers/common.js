const tokenName = 'SIEGE-OF-THE-CITADEL-TOKEN'

// Takes the request object and returns it as an object
export async function formToObj(request){
  const formData = await request.formData()
  return Object.fromEntries(formData.entries())
}