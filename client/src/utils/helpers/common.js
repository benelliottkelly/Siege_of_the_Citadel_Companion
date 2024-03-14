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

// Function to determin which user is logged in
export function getUser(){
  const token = getToken()
  if (!token) {
    return null
  }
  const b64 = token.split('.')[1]
  const payload = JSON.parse(atob(b64))
  console.log(payload.user_id)
  // if (payload.user_id === user){
  //   return true
  // } else {
  //   return false
  // }
}