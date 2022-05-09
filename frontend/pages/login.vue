<template>
  <NuxtLayout name="blank">
    <div
      class="min-h-screen flex flex-col sm:justify-center items-center pt-6 sm:pt-0"
    >
      <div class="text-h2 text-4xl">Journal</div>

      <div class="w-full sm:max-w-md mt-6 px-6 py-4 bg-white overflow-hidden">
        <form method="POST" action="#" data-bitwarden-watching="1">
          <!-- <input
            type="hidden"
            name="_token"
          /> -->
          <div>
            <label class="block font-medium text-base" for="email">
              Email
            </label>
            <input
              class="border-black border-2 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 rounded-md shadow-sm block w-full mt-1 py-2 indent-2"
              id="email"
              type="email"
              name="email"
              required
              autofocus
            />
          </div>

          <div class="mt-4">
            <label class="block font-medium text-base" for="password">
              Password
            </label>
            <input
              class="border-black border-2 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 rounded-md shadow-sm block w-full mt-1 py-2 indent-2"
              id="password"
              type="password"
              name="password"
              required
            />
          </div>

          <div class="block mt-4">
            <label for="remember_me" class="flex items-center">
              <input
                type="checkbox"
                class="rounded border-gray-300 text-black shadow-sm focus:border-gray-500 focus:ring focus:ring-gray-200 focus:ring-opacity-50"
                id="remember_me"
                name="remember"
              />
              <span class="ml-2 text-sm">Remember me</span>
            </label>
          </div>

          <div class="flex items-center justify-end mt-4 space-x-4">
            <a class="text-gray" href="#">
              <span> Forgot your password? </span>
            </a>

            <BtnBlack> Log in </BtnBlack>
          </div>
        </form>
      </div>
    </div>
  </NuxtLayout>
</template>
