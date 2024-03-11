const tokenName = 'SIEGE-OF-THE-CITADEL-TOKEN'

// Takes the request object and returns it as an object
export async function formToObj(request){
  const formData = await request.formData()
  return Object.fromEntries(formData.entries())
}

// Save JWT Token to local storage
export function setToken(token){
  localStorage.setItem(tokenName, token)
}

// Get JWT Token from local storage
export function getToken(){
  return localStorage.getItem(tokenName)
}

// Remove the JWT Token from local storage
export function removeToken(){
  console.log('logged out')
  localStorage.removeItem(tokenName)
}

// Function returning true or false based on local storage token
export function doesTokenExist(){
  const token = getToken()
  if (!token) {
    return false
  } else {
    return true
  }
}