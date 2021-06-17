import AssertionException from "@/business/utils/AssertionException";

export default class Assert {
    /**
     * Fail if the given condition is false (and throw an AssertionError with the provided message).
     *
     * @param condition
     * @param message
     */
    static assert(condition, message) {
        if (!condition) {
            throw new AssertionException(message);
        }
    }
}
