package com.themaskedcrusader.advent15.days;

import java.io.File;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class Day_04 extends AdventDay {
    String problem = "day_3";

    @Override
    public void execute(File directory) {
        String input = "ckczppom";
        partOne(input);
        partTwo(input);
    }

    void partOne(String input) {
        int answer = md5sumCheck(input, "00000");
        System.out.println("Part 1: lowest number solution : " + answer);
    }

    void partTwo(String input) {
        int answer = md5sumCheck(input, "000000");
        System.out.println("Part 2: lowest number solution : " + answer);
    }

    int md5sumCheck(String input, String compare) {
        int ret = 0;
        try {
            MessageDigest md = MessageDigest.getInstance("MD5");
            for (;; ++ret) {
                String test = input + ret;
                md.update(test.getBytes());
                byte[] digest = md.digest();
                String hash = byteToHex(digest);
                if (hash.startsWith(compare)) break;
            }
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
        }
        return ret;
    }

    String byteToHex(byte[] bytes) {
        StringBuilder sb = new StringBuilder();
        for (byte b : bytes) {
            sb.append(String.format("%02X", b));
        }
        return sb.toString();
    }
}
