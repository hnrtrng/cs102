# STEAM for Vietnam - CS 102 

Xem ghi chú tóm tắt các bài học: [LINK](https://github.com/STEAMforVietnam/cs102/tree/lesson-notes/notes)

## Miêu tả dự án

**Xin chào! Mình là Thanh Hải, và đây là sản phẩm dự án cuối khóa của mình, được phát triển dựa trên nền trò chơi STEAM Valley của STEAM For Vietnam.**

**Những thay đổi so với sản phẩm gốc của S4V:**

- Game có 20 màn chơi, 10 màn đầu là màn chính, còn 10 màn sau là màn extra
- Thêm nhạc và hình nền mới cho hầu hết các màn chơi
- Thu nhỏ các entities trong game để người chơi di chuyển lên xuống nhiều hơn
- Thay 3 trái tim của người chơi bằng 1 thanh máu chứa 100 HP
- Thêm các entities mới:
    + 2 NPCs ở màn 4 và 9
    + Vật nhọn (spikes): Người chơi sẽ mất máu dần dần nếu tiếp xúc với vật nhọn. Mẹo: nếu kẹt trong vật sắc nhọn thì ấn nút di chuyển liên tục để thoát ra.
    + Hộp hồi máu (extra_hp_box): Hồi 20 máu nếu người chơi chạm vào hộp
- Người chơi chỉ được ném 1 burger sau mỗi 0.25 giây, thay vì trước đây có thể ném liên tục không giới hạn thời gian
- Các bóng ma bình thường cũng có thể phóng đạn giống boss, cụ thể từ 1-4 đạn
- Đạn của người chơi và bóng ma có thể nhảy trên bạt nhún
- Vận dụng những chức năng đặc biệt của burger và bóng ma. Điều này được thể hiện cụ thể ở màn 5-10 và 15-20.
- Thêm một số thay đổi lặt vặt khác. Bạn có thể xem tất cả những thay đổi ở đây: https://github.com/hnrtrng/cs102/compare/master...final-project

**LƯU Ý:**

- Một số màn chơi sẽ bị lag nhiều hơn các màn chơi khác, do mình thêm vào quá nhiều bóng mà và chúng bắn ra quá nhiều đạn.
- Khi hoạt động, game sẽ có khả năng bị lỗi "Fatal Python Error: (pygame parachute) Segmentation fault" do tải lên quá nhiều entities. Khi đó, hãy thử chạy lại game.
(mình xin các bạn thông cảm giùm mình, đó là cái giá mình nhận khi mình muốn làm 1 game hay.)

**Còn bây giờ, mình mong các bạn thưởng thức trò chơi nhé!**
    
## Đường dẫn đến phiên bản cuối mỗi bài học

1. [Crazy Robot](https://github.com/STEAMforVietnam/cs102/tree/ls1/)
2. [Crazy Robot](https://github.com/STEAMforVietnam/cs102/tree/ls2-5)
3. Bài học ôn tập Python căn bản
4. [Thách thức giới hạn](https://github.com/STEAMforVietnam/cs102/tree/ls4-5)
5. Bài đặc biệt về thiết kế trò chơi và công cụ Figma
6. [Bí Ẩn STEAM Valley](https://github.com/STEAMforVietnam/cs102/tree/ls6-final)
7. [Lần theo dấu vết](https://github.com/STEAMforVietnam/cs102/tree/ls7-final)
8. Bài đặc biệt về thiết kế trò chơi và công cụ Figma
9. [Tìm kiếm sức mạnh](https://github.com/STEAMforVietnam/cs102/tree/ls9-five)
10. [Vượt qua đối thủ đáng gờm](https://github.com/STEAMforVietnam/cs102/tree/ls10-four)
11. [Năng lượng hạnh phúc](https://github.com/STEAMforVietnam/cs102/tree/ls11-final)
12. [Khúc ca chiến thắng](https://github.com/STEAMforVietnam/cs102/tree/master)
