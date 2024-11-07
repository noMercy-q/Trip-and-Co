import {createStore} from 'vuex'

export default createStore({
    state: {
        auth: {
            token: localStorage.getItem('token'),
        }
    },
    getters: {
        isAuthenticated: (state) => !!state.auth.token,
    },
    mutations: {
        setToken(state, token) {
            state.auth.token = token

            localStorage.setItem('token', token)
        },
        clearToken(state) {
            state.auth.token = null;

            localStorage.removeItem('token')
        },
    },
    actions: {
        login({commit}, token) {
            commit('setToken', token);
        },
        logout({commit}) {
            commit('clearToken');
        },
    },
    modules: {}
})


/*

// store/index.js
export default new Vuex.Store({
  state: {
    auth: {
      token: null, // Здесь хранится токен
    },
  },
  mutations: {
    setToken(state, token) {
      state.auth.token = token;
    },
    clearToken(state) {
      state.auth.token = null;
    },
  },
  actions: {
    login({ commit }, token) {
      commit('setToken', token);
    },
    logout({ commit }) {
      commit('clearToken');
    },
  },
  getters: {
    isAuthenticated: (state) => !!state.auth.token,
  },
});

 */