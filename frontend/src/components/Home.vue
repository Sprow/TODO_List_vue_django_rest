<template>
<div class="home">
    <ul>
        TODO list
        <li v-for="(item, index) in list_of_tasks" :key="item.id">
            <div v-if=item.task_status>
                <input v-on:click="change_status" :id="('label_')+item.id" type="checkbox" checked>
                <label :for="('label_')+index">{{ item.text }}</label>
                <span v-on:click="delete_element(index, item.id)" :id="('delete_')+item.id">&#10008;</span>
            </div>
            <div v-else>
                <input v-on:click="change_status" :id="('label_')+item.id" type="checkbox">
                <label :for="('label_')+index">{{ item.text }} </label>
                <span v-on:click="delete_element(index, item.id)" :id="('delete_')+item.id">&#10008;</span>
            </div>
        </li>
    </ul>

    <form id="add_task_form" v-on:submit="checkForm" method="POST">
      <p>
        <label for="name">New task: </label>
        <input type="text" name="name" id="name" v-model="name">
        <input type="submit" value="add">
      </p>
    </form>
</div>
</template>

<script>
    import axios from 'axios';

    export default {
        name: "Home",
        data() {
            return {
                list_of_tasks: null,
                name: ''
            }
        },
        mounted() {
            axios
              .get('http://127.0.0.1:8000/todo_list/api/list?format=json')
              .then(response => (this.list_of_tasks = response.data));
        },
        methods: {
            change_status: function (event) {
                axios
                    .put('http://127.0.0.1:8000/todo_list/task/update/'+event.target.id.split('_')[1]);
            },

            delete_element: function (index, id) {
                axios
                    .delete('http://127.0.0.1:8000/todo_list/task/delete/'+ id);
                this.list_of_tasks.splice(index, 1)
            },

            checkForm: function (event) {
                event.preventDefault();
                if (0 < this.name.length < 200) {
                    let data = {'text': this.name, 'task_status': false};
                    axios
                        .post('http://127.0.0.1:8000/todo_list/task/create', data)
                        .then(response => (this.list_of_tasks.push(response.data)))
                }
            }
        }
    }

</script>

<style scoped>
    .home {
        font-size: 25px;
    }
    li {
        list-style: none
    }
</style>